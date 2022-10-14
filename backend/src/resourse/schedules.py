from flask_restful import reqparse
from src.app import app
from src.model.course import Course
from src.model.schedule import Schedule


@app.route("/schedule", methods=['POST'])
def add_schedule():
    parser = reqparse.RequestParser()
    parser.add_argument('courseid', type=int, required=True, help='This field cannot be left blank')
    parser.add_argument('schedules', type=dict, action='append', required=True, help='This field cannot be left blank')
    data = parser.parse_args()

    courseId = data["courseid"]
    course_entity = Course.query.get(courseId)

    for schedule in data['schedules']:
        start = schedule['start']
        end = schedule['end']
        participants = int(schedule['participants'])

        schedule_entity = Schedule(start=start, end=end, participants=participants, course_id=courseId)
        course_entity.schedules.append(schedule_entity)
        schedule_entity.save_to_db()

    return {'message': 'schedules have been created successfully.'}


@app.route("/schedule/<courseId>", methods=['GET'])
def get_schedule(courseId: int):
    course_entity = Course.query.get(courseId)

    if course_entity:
        return {"schedules": [schedule.return_one() for schedule in course_entity.schedules]}
    else:
        return {"message": "course not found"}
