from app import app
from flask_restful import reqparse
from .models import User, RevokedTokenModel, Role, Subscription_type
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
    parser.add_argument('email', help='email cannot be blank', required=True)

    data = parser.parse_args()
    username = data['username']
    email = data['email']

    if User.find_by_username(username):
        return {'message': f'User {username} already exists'}

    new_user = User(
        username=username,
        password=User.generate_hash(data['password'], ),
        email=email
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
        return {'message': "Wrong credentials"}


@app.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']

    try:
        revoked_token = RevokedTokenModel(jti=jti)
        revoked_token.add()

        return {'message': 'Access token has been revoked'}
    except:
        return {'message': 'Something went wrong'}, 500


@app.route('/logout/refresh', methods=['POST'])
@jwt_required(refresh=True)
def logout_refresh():
    jti = get_jwt()['jti']

    try:
        revoked_token = RevokedTokenModel(jti=jti)
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


@app.route('/users', methods=['DELETE'])
def delete_users():
    return User.delete_all()


@app.route('/secret', methods=['GET'])
@jwt_required()
def secret_resource():
    return {'secrets': 'are now open to you'}

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
