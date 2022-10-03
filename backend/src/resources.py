from flask_login import login_required
from flask_restful import Resource, reqparse
from app import app
from .models import User, RevokedTokenModel, Role
from flask_user import roles_required

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
)

import pdb

parser = reqparse.RequestParser()

parser.add_argument('username', help='username cannot be blank', required=True)
parser.add_argument('password', help='password cannot be blank', required=True)


@app.route('/registration', methods=['POST'])
def register():
    data = parser.parse_args()
    username = data['username']

    if User.find_by_username(username):
        return {'message': f'User {username} already exists'}

    new_user = User(
        username=username,
        password=User.generate_hash(data['password']),
    )
    role = Role(name="user")

    new_user.roles.append(role)

    try:
        print(0)

        new_user.save_to_db()
        print(1)

        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)
        print(2)

        return {
            'message': f'User {username} was created',
            'access_token': access_token,
            'refresh_token': refresh_token
        }
    except:
        return {'message': 'Something went wrong'}, 500


@app.route('/login', methods=['POST'])
def login():
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


@app.route('/logout', methods=['POST'])
@jwt_required(refresh=True)
def logout_refresh():
    jti = get_jwt()['jti']

    try:
        revoked_token = RevokedTokenModel(jti=jti)
        revoked_token.add()
        pdb.set_trace()

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
def get_users():
    current_user = get_jwt_identity()
    user = User.find_by_username(current_user)
    if "admin" in user.roles:
        return User.return_all()
    return "No permission", 403


@app.route('/users', methods=['DELETE'])
def delete_users():
    return User.delete_all()


@app.route('/secret', methods=['GET'])
@jwt_required()
def secret_resource():
    return {'secrets': 'are now open to you'}
