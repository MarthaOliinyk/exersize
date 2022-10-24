from flask_restful import reqparse
from src.app import app
from src.model.course import Course
from src.model.schedule import Schedule

from src.utils import coach_required

from flask_jwt_extended import jwt_required


@app.route('/schedule', methods=['POST'])
@jwt_required()
@coach_required
def add_schedule():
    parser = reqparse.RequestParser()
    parser.add_argument('courseid', type=int, required=True, help='This field cannot be left blank')
    parser.add_argument('schedules', type=dict, action='append', required=True, help='This field cannot be left blank')
    data = parser.parse_args()

    course_id = data['courseid']
    course_entity = Course.query.get(course_id)
    if course_entity:
        for schedule in data['schedules']:
            start = schedule['start']
            end = schedule['end']
            participants = int(schedule['participants'])

            schedule_entity = Schedule(start=start, end=end, participants=participants, course_id=course_id)
            course_entity.schedules.append(schedule_entity)
            schedule_entity.save_to_db()

        return {'message': 'schedules have been created successfully.'}
    else:
        return {'message': 'course not found.'}


@app.route('/schedule/course/<courseId>', methods=['GET'])
def get_schedule_by_course_id(courseId: int):
    course_entity = Course.query.get(courseId)

    if course_entity:
        return {'schedules': [schedule.return_one() for schedule in course_entity.schedules]}
    else:
        return {'message': 'course not found'}


@app.route('/schedule', methods=['GET'])
@jwt_required()
def get_schedules():
    return Schedule.return_all()


@app.route('/schedule/<scheduleId>', methods=['GET'])
@jwt_required()
def get_schedule_by_id(scheduleId: int):
    return Schedule.get_by_id(scheduleId)


@app.route('/schedule/<scheduleId>', methods=['DELETE'])
@jwt_required()
@coach_required
def delete_schedule_by_id(scheduleId: int):
    return Schedule.delete_by_id(scheduleId)


@app.route('/schedule', methods=['PUT'])
@jwt_required()
@coach_required
def update_schedule():
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, required=True, help='This field cannot be left blank')
    parser.add_argument('start', required=True, help='This field cannot be left blank')
    parser.add_argument('end', required=True, help='This field cannot be left blank')
    parser.add_argument('participants', type=int, required=True, help='This field cannot be left blank')
    parser.add_argument('courseid', type=int, required=True, help='This field cannot be left blank')
    data = parser.parse_args()

    schedule_id = data['id']
    schedule_entity = Schedule.query.get(schedule_id)

    if schedule_entity:
        schedule_entity.start = data['start']
        schedule_entity.end = data['end']
        schedule_entity.participants = data['participants']
        schedule_entity.course_id = data['courseid']
        schedule_entity.save_to_db()

        return {'message': 'Schedule have been updated successfully.'}
    else:
        return {'error': f'Schedule with id={schedule_id} does not exist!'}, 404
