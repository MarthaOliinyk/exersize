from src.app import app
from flask_restful import reqparse
from src.model.subscription import Subscription
from src.model.subscription_type import SubscriptionType
from src.model.user import User
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)
from datetime import datetime, timedelta


@app.route("/subscription", methods=['POST'])
@jwt_required()
def add_subscription():
    parser = reqparse.RequestParser()
    parser.add_argument('start', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('subscription_type_id', type=int, required=True, help='This field cannot be left blank')
    data = parser.parse_args()

    current_user = get_jwt_identity()
    user = User.find_by_username(current_user)

    subscription_type = SubscriptionType.query.get(data["subscription_type_id"])
    if subscription_type:
        end = datetime.strptime(data["start"], "%Y-%m-%d") + timedelta(days=subscription_type.duration)

        subscription_entity = Subscription(start=data["start"], end=end,
                                           session_number=subscription_type.session_count
                                           , user_id=user.id, subscription_type_id=data["subscription_type_id"])
        user.subscriptions.append(subscription_entity)
        subscription_type.subscriptions.append(subscription_entity)

        subscription_entity.save_to_db()

        return {'message': 'subscription has been created successfully.'}
    else:
        return {'message': 'subscription type not found.'}


@app.route("/subscription/user/<userId>", methods=['GET'])
@jwt_required()
def get_subscriptions_by_userid(userId: int):
    user_entity = User.query.get(userId)

    if user_entity:
        return {"subscriptions": [subscription.return_one() for subscription in user_entity.subscriptions]}
    else:
        return {"message": "user not found"}


@app.route('/subscription/<subId>', methods=['GET'])
@jwt_required()
def get_subscription_by_id(subId: int):
    return Subscription.get_by_id(subId)


@app.route("/subscription/<subId>", methods=['DELETE'])
@jwt_required()
def delete_subscription_by_id(subId: int):
    return Subscription.delete_by_id(subId)
