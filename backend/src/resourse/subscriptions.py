from src.app import app
import requests
from flask_restful import reqparse
from src.model.subscription import Subscription
from src.model.subscription_type import SubscriptionType
from src.model.user import User
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)
from random import randint
from datetime import timedelta, date
import base64
from hashlib import sha1
from flask import request
import json


def add_subscription(userid, subscription_type_id):
    user = User.query.get(userid)
    subscription_type = SubscriptionType.query.get(subscription_type_id)

    if subscription_type and user:
        start = date.today()
        end = start + timedelta(days=subscription_type.duration)

        subscription_entity = Subscription(start=start, end=end,
                                           session_number=subscription_type.session_count
                                           , user_id=userid, subscription_type_id=subscription_type_id)

        user.subscriptions.append(subscription_entity)
        subscription_type.subscriptions.append(subscription_entity)

        subscription_entity.save_to_db()

        return 200
    return 404


@app.route('/subscriptions', methods=['GET'])
@jwt_required()
def get_subscriptions_by_userid():
    current_user = get_jwt_identity()
    user = User.find_by_username(current_user)

    if user:
        return {'subscriptions': [subscription.return_one() for subscription in user.subscriptions]}
    else:
        return {'error': 'user not found'}, 404


@app.route('/subscription/<subId>', methods=['GET'])
@jwt_required()
def get_subscription_by_id(subId: int):
    return Subscription.get_by_id(subId)


@app.route('/subscription/<subId>', methods=['DELETE'])
@jwt_required()
def delete_subscription_by_id(subId: int):
    return Subscription.delete_by_id(subId)


@app.route('/create/payment', methods=['POST'])
@jwt_required()
def payment_create():
    parser = reqparse.RequestParser()
    parser.add_argument('subscription_type_id', type=int, required=True, help='This field cannot be left blank')
    data_parse = parser.parse_args()
    username = get_jwt_identity()
    user = User.find_by_username(username)
    user_id = user.id
    sub_type = SubscriptionType.query.get(data_parse["subscription_type_id"])

    private_key = "sandbox_QSenQtvw4T7PDwTXG8ur9gXFzCD02yZSqCpC1rsH"
    public_key = "sandbox_i45987901491"

    data = {}

    data['version'] = 3
    data['public_key'] = public_key
    data['action'] = "pay"
    data["amount"] = sub_type.price
    data["currency"] = "UAH"
    data["language"] = "uk"
    data["description"] = f"Pay for {sub_type.name} subscription."
    data["order_id"] = randint(0, 10000)
    data['server_url'] = 'https://bbbf-46-211-172-63.eu.ngrok.io/callback/payment'
    data["customer"] = user_id
    data["product_description"] = sub_type.id

    data_encd = base64.b64encode(json.dumps(data).encode("utf-8")).decode("ascii")
    signature = base64.b64encode(sha1((private_key + data_encd + private_key).encode("utf-8")).digest())

    params = {"data": data_encd, "signature": signature}

    res = requests.post(url='https://www.liqpay.ua/api/3/checkout', data=params)

    if res.status_code == 200:
        return {"payment_url": res.url}
    else:
        return {"error": "Payment error"}, 404


@app.route('/callback/payment', methods=['POST'])
def payment_callback():
    private_key = "sandbox_QSenQtvw4T7PDwTXG8ur9gXFzCD02yZSqCpC1rsH"

    data_raw = request.values
    signature = base64.b64encode(sha1((private_key + data_raw["data"] + private_key).encode("utf-8")).digest())

    if signature == data_raw["signature"].encode("utf-8"):
        data = json.loads(base64.b64decode(data_raw["data"]).decode("utf-8"))
        if data["status"] == "success":
            user_id = int(data["customer"])
            subscription_type_id = int(data["product_description"])
            res = add_subscription(user_id, subscription_type_id)
            if res == 200:
                return {'message': 'Payment was successful'}
            else:
                return {"error": "Error create subscription"}, 404
        return {"error": f"Payment status: {data['status']}"}, 403
    return {"error": "Wrong signature"}, 403
