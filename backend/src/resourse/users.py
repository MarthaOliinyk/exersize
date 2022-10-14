from src.app import app
from src.model.user import User
from src.utils import admin_required
from flask_jwt_extended import jwt_required


@app.route('/users/<userId>', methods=['GET'])
@jwt_required()
@admin_required
def get_user_by_id(userId: int):
    return User.get_by_id(userId)


@app.route('/users', methods=['GET'])
@jwt_required()
@admin_required
def get_users():
    return User.get_all()


@app.route('/users/<userId>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_user_by_id(userId: int):
    return User.delete_by_id(userId)
