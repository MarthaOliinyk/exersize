from src.app import app
from flask_restful import reqparse
from src.model.course import Course
from src.model.subscription_type import SubscriptionType

from src.utils import coach_required

from flask_jwt_extended import jwt_required


@app.route("/subscriptions/types/course/<courseId>", methods=['GET'])
def get_subscription_type_by_courseid(courseId: int):
    course_entity = Course.query.get(courseId)

    if course_entity:
        return {"subscription_types": [subscription.return_one() for subscription in course_entity.subscription_types]}
    else:
        return {"message": "course not found"}


@app.route('/subscriptions/types', methods=['GET'])
@jwt_required()
def get_subscription_types():
    return SubscriptionType.return_all()


@app.route('/subscriptions/types/<sub_typeId>', methods=['GET'])
@jwt_required()
def get_subscription_type_by_id(sub_typeId: int):
    return SubscriptionType.get_by_id(sub_typeId)


@app.route("/subscriptions/types/<sub_typeId>", methods=['DELETE'])
@jwt_required()
@coach_required
def delete_subscription_type_by_id(sub_typeId: int):
    return SubscriptionType.delete_by_id(sub_typeId)


@app.route("/subscriptions/types", methods=['PUT'])
@jwt_required()
@coach_required
def update_subscription_type():
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, required=True, help='This field cannot be left blank')
    parser.add_argument('name', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('session_count', type=int, required=True, help='This field cannot be left blank')
    parser.add_argument('duration', type=int, required=True, help='This field cannot be left blank')
    parser.add_argument('price', type=float, required=True, help='This field cannot be left blank')
    parser.add_argument('courseid', type=int, required=True, help='This field cannot be left blank')
    data = parser.parse_args()

    sub_typeId = data["id"]
    sub_type_entity = SubscriptionType.query.get(sub_typeId)

    if sub_type_entity:
        sub_type_entity.name = data["name"]
        sub_type_entity.session_count = data["session_count"]
        sub_type_entity.duration = data["duration"]
        sub_type_entity.price = data["price"]
        sub_type_entity.course_id = data["courseid"]
        sub_type_entity.save_to_db()

        return {'message': 'Subscription type have been updated successfully.'}
    else:
        return {'error': f'Subscription type with id={sub_typeId} does not exist!'}, 404
