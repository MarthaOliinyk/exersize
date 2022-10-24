from src.app import app
from flask_restful import reqparse
from src.model.subscription_type import SubscriptionType
from src.model.user import User

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
)

from backend.src.model.appointment import Appointment
from backend.src.model.schedule import Schedule
from backend.src.model.subscription import Subscription


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

    new_appointment = Appointment(
        time=time,
        schedule_id=schedule_id,
    )
    new_appointment.save_to_db()

    user.appointments.append(new_appointment)
    user.save_to_db()

    subscription = Schedule.query.join(SubscriptionType, Schedule.course_id == SubscriptionType.course_id).\
        join(Subscription, Subscription.subscription_type_id == SubscriptionType.id).\
        join(User, Subscription.user_id == User.id).\
        filter(Schedule.id == schedule_id)

    subscription.session_number -= 1

    return {'message': 'appointment have been created successfully.'}, 201


@app.route('/appointment/<appointment_id>', methods=['GET'])
@jwt_required()
def get_appointment_by_id(appointment_id: int):
    return Appointment.get_by_id(appointment_id)
