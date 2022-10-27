from src.app import app
from flask_restful import reqparse
from src.model.subscription_type import SubscriptionType
from src.model.user import User

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
)

from src.model.appointment import Appointment
from src.model.schedule import Schedule


@app.route('/appointment', methods=['POST'])
@jwt_required()
def add_appointment():
    parser = reqparse.RequestParser()
    parser.add_argument('time', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('schedule_id', type=int, required=True, help='This field cannot be left blank')
    data = parser.parse_args()

    time = data['time']
    schedule_id = data['schedule_id']

    current_user = get_jwt_identity()
    user = User.find_by_username(current_user)

    schedule = Schedule.query.get(schedule_id)

    new_appointment = Appointment(
        time=time,
        schedule_id=schedule_id,
    )

    user.appointments.append(new_appointment)
    schedule.appointments.append(new_appointment)

    for subscription in user.subscriptions:
        sub_type = SubscriptionType.query.get(subscription.subscription_type_id)
        if sub_type.course_id == schedule.course_id:
            if subscription.session_number >= 1:
                subscription.session_number -= 1
            else:
                return {'message': 'no sessions in subscription.'}, 402
            break
    new_appointment.save_to_db()

    return {'message': 'appointment have been created successfully.'}, 201


@app.route('/appointment/<appointment_id>', methods=['GET'])
@jwt_required()
def get_appointment_by_id(appointment_id: int):
    return Appointment.get_by_id(appointment_id)
