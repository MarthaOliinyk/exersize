from src.app import app
from flask_restful import reqparse
from src.model.course import Course
from src.model.subscription_type import SubscriptionType
from src.model.user import User
from src.utils import coach_required

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
)
from datetime import timedelta


@app.route('/courses', methods=['POST'])
@jwt_required()
@coach_required
def add_course():
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('description', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('tag', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('sub_type', type=dict, action='append', required=True, help='This field cannot be left blank')
    data = parser.parse_args()

    name = data['name']
    description = data['description']
    tag = data['tag']

    current_user = get_jwt_identity()
    user = User.find_by_username(current_user)

    new_course = Course(
        name=name,
        description=description,
        tag=tag
    )
    new_course.save_to_db()

    user.courses.append(new_course)
    user.save_to_db()

    course_id = Course.get_id(name)

    for s_type in data['sub_type']:
        name = s_type['name']
        session_count = s_type['count']
        duration = int(s_type['duration'])
        price = float(s_type['price'])
        subscription_type = SubscriptionType(name=name, session_count=session_count, duration=duration,
                                             price=price, course_id=course_id)
        subscription_type.save_to_db()

    return {'message': 'course and sub type have been created successfully.'}, 201


@app.route('/courses', methods=['GET'])
@jwt_required()
def get_all_courses():
    return Course.return_all()


@app.route('/courses/<course_id>', methods=['GET'])
@jwt_required()
def get_course_by_name(course_id: int):
    return Course.return_one(course_id)


@app.route('/courses/<course_id>', methods=['DELETE'])
@jwt_required()
@coach_required
def delete_course(course_id: int):
    try:
        Course.delete_by_id(course_id)
        return {'message': 'Course and subscriptions were deleted'}
    except:
        return {'error': 'Something went wrong'}, 500


@app.route('/courses/<course_id>', methods=['PUT'])
@jwt_required()
@coach_required
def update_course(course_id: int):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('description', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('tag', type=str, required=True, help='This field cannot be left blank')
    data = parser.parse_args()
    return Course.update_by_id(course_id, data)


@app.route('/courses/search/<text>', methods=['GET'])
@jwt_required()
def get_serched_courses(text: str):
    return Course.search_courses(text)


@app.route('/courses/filter', methods=['GET'])
@jwt_required()
def get_filtered_types():
    parser = reqparse.RequestParser()
    parser.add_argument('tag', type=str, required=False, default=Course.tag)
    parser.add_argument('duration', type=int, required=False, default=SubscriptionType.duration)
    parser.add_argument('price', type=float, required=False, default=SubscriptionType.price)
    data = parser.parse_args()
    return SubscriptionType.get_filtered(data)


@app.route('/courses/schedule/<course_id>', methods=['GET'])
def get_course_schedule(course_id: int):
    course_entity = Course.query.get(course_id)
    res = []
    for schedule in course_entity.schedules:
        appointments_time = [ap.time for ap in schedule.appointments]
        time = schedule.start
        while time <= schedule.end:
            members = appointments_time.count(time)
            res.append({"time":time, "free": schedule.participants - members})
            time = time + timedelta(hours=1)

    return {"times": res}
    
