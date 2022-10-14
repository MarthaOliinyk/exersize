from src.app import app
from src.model.user import User

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
)


@app.route('/users/roles', methods=['GET'])
@jwt_required()
def get_user_roles():
    current_user = get_jwt_identity()
    user = User.find_by_username(current_user)

    def to_json(role):
        return {'role': role.name}

    return {'roles': [to_json(role) for role in user.roles]}
