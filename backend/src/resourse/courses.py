from src.app import app
from flask_restful import reqparse
from src.model.course import Course
from src.model.subscription_type import SubscriptionType
from src.model.user import User
from src.model.schedule import Schedule
from src.utils import coach_required

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
)


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
def get_courses():
    return Course.return_all()


@app.route('/courses', methods=['DELETE'])
def delete_courses():
    return Course.delete_all()


@app.route("/subscriptions/types/<courseId>", methods=['GET'])
def get_subscription_type(courseId: int):
    course_entity = Course.query.get(courseId)

    if course_entity:
        return {"subscription_types": [subscription.return_one() for subscription in course_entity.subscription_types]}
    else:
        return {"message": "course not found"}


@app.route('/subscriptions/types', methods=['GET'])
def get_subscription_types():
    return SubscriptionType.return_all()
