import sys
from datetime import datetime, timezone, timedelta
from flask import jsonify
from src.app import app
from flask_restful import reqparse
from src.model.revoked_tokens import RevokedTokens
from src.model.role import Role
from src.model.user import User

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    get_jwt,
    set_access_cookies,
    unset_jwt_cookies
)


@app.route('/registration', methods=['POST'])
def register():
    parser = reqparse.RequestParser()

    parser.add_argument('username', help='username cannot be blank', required=True)
    parser.add_argument('password', help='password cannot be blank', required=True)
    parser.add_argument('fullname', help='fullname cannot be blank', required=True)
    parser.add_argument('email', help='email cannot be blank', required=True)
    parser.add_argument('age', help='age cannot be blank', required=True)

    data = parser.parse_args()
    username = data['username']
    email = data['email']
    fullname = data['fullname']
    age = int(data['age'])

    if User.find_by_username(username):
        return {'message': f'User {username} already exists'}, 403

    if User.find_by_email(email):
        return {'message': f'User with email {email} already exists'}, 403

    new_user = User(
        username=username,
        password=User.generate_hash(data['password']),
        email=email,
        fullname=fullname,
        age=age
    )
    role = Role.find_by_name('user')

    new_user.roles.append(role)

    try:
        new_user.save_to_db()

        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)

        response = jsonify({
            'message': f'User {username} was created',
            'access_token': access_token,
            'refresh_token': refresh_token
        })
        set_access_cookies(response, access_token)

        return response, 200
    except:
        return {'error': f'{sys.exc_info()[0]}'}, 500


@app.route('/login', methods=['POST'])
def login():
    parser = reqparse.RequestParser()

    parser.add_argument('username', help='username cannot be blank', required=True)
    parser.add_argument('password', help='password cannot be blank', required=True)

    data = parser.parse_args()
    username = data['username']

    current_user = User.find_by_username(username)

    if not current_user:
        return {'message': f'User {username} doesn\'t exist'}

    if User.verify_hash(data['password'], current_user.password):
        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)

        response = jsonify({
            'message': f'Logged in as {username}',
            'access_token': access_token,
            'refresh_token': refresh_token
        })

        set_access_cookies(response, access_token)
        return response, 200
    else:
        return {'error': 'Wrong credentials'}, 401


@app.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']

    try:
        revoked_token = RevokedTokens(jti=jti)
        revoked_token.add()

        response = jsonify({'message': 'Access token has been revoked'})
        unset_jwt_cookies(response)
        return response, 200
    except:
        return {'error': f'{sys.exc_info()[0]}'}, 500


@app.route('/users/password', methods=['PUT'])
@jwt_required()
def change_password():
    parser = reqparse.RequestParser()

    parser.add_argument('old_password', help='password cannot be blank', required=True)
    parser.add_argument('new_password', help='new password cannot be blank', required=True)
    parser.add_argument('confirm_password', help='confirm password cannot be blank', required=True)

    data = parser.parse_args()

    current_user = get_jwt_identity()
    user = User.find_by_username(current_user)
    old_password = data['old_password']
    new_password = data['new_password']
    confirm_password = data['confirm_password']

    if not User.verify_hash(old_password, user.password):
        return {'error': 'Old password is invalid'}, 400

    if new_password != confirm_password:
        return {'error': 'New password doesn\'t match'}, 400

    if old_password == new_password:
        return {'error': 'New password is the same'}, 400

    user.password = User.generate_hash(new_password)
    user.save_to_db()

    return {'message': 'password was changed'}, 200


@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()['exp']
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        return response


@app.route('/logout/refresh', methods=['POST'])
@jwt_required(refresh=True)
def logout_refresh():
    jti = get_jwt()['jti']

    try:
        revoked_token = RevokedTokens(jti=jti)
        revoked_token.add()

        return {'message': 'Refresh token has been revoked'}
    except:
        return {'error': f'{sys.exc_info()[0]}'}, 500


@app.route('/token/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)

    return {'access_token': access_token}
