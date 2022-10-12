from app import app
from flask_restful import reqparse
from .models import User, RevokedTokens, Role, Subscription_type
from .utils import admin_required, coach_required, user_required

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
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

        return {
            'message': f'User {username} was created',
            'access_token': access_token,
            'refresh_token': refresh_token
        }
    except:
        return {'message': 'Something went wrong'}, 500


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

        return {
            'message': f'Logged in as {username}',
            'access_token': access_token,
            'refresh_token': refresh_token
        }
    else:
        return {'message': "Wrong credentials"}, 401


@app.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']

    try:
        revoked_token = RevokedTokens(jti=jti)
        revoked_token.add()

        return {'message': 'Access token has been revoked'}
    except:
        return {'message': 'Something went wrong'}, 500


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
        return {'message': 'Old password is invalid'}, 400

    if new_password != confirm_password:
        return {'message': 'New password doesn\'t match'}, 400

    if old_password == new_password:
        return {'message': 'New password is the same'}, 400

    user.password = User.generate_hash(new_password)
    user.save_to_db()

    return {'message': 'password was changed'}, 200


@app.route('/logout/refresh', methods=['POST'])
@jwt_required(refresh=True)
def logout_refresh():
    jti = get_jwt()['jti']

    try:
        revoked_token = RevokedTokens(jti=jti)
        revoked_token.add()

        return {'message': 'Refresh token has been revoked'}
    except:
        return {'message': 'Something went wrong'}, 500


@app.route('/token/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)

    return {'access_token': access_token}


@app.route('/users', methods=['GET'])
@jwt_required()
@admin_required
def get_users():
    return User.return_all()


@app.route('/users/roles', methods=['GET'])
@jwt_required()
def get_user_roles():
    current_user = get_jwt_identity()
    user = User.find_by_username(current_user)

    def to_json(role):
        return {'role': role.name}

    return {'roles': [to_json(role) for role in user.roles]}


@app.route('/users', methods=['DELETE'])
def delete_users():
    return User.delete_all()

@app.route('/subscription_type', methods=['POST'])
def add_subscription_type():
    parser = reqparse.RequestParser()

    parser.add_argument('name', help='name cannot be blank', required=True)
    parser.add_argument('session_count', help='session count cannot be blank', required=True)
    parser.add_argument('duration', help='duration cannot be blank', required=True)
    parser.add_argument('price', help='price cannot be blank', required=True)
    parser.add_argument('course_id', help='course id cannot be blank', required=True)

    data = parser.parse_args()
    name = data["name"]

    new_subscription_type = Subscription_type(
        name=name,
        session_count=data["session_count"],
        duration=data["duration"],
        price=data["price"],
        course_id=data["course_id"]
    )

    try:
        new_subscription_type.add()

        return {'message': f'Subscription type {name} was created'}
    except:
        return {'message': 'Something went wrong'}, 500
