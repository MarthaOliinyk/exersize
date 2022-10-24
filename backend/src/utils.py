from src.model.user import User
from functools import wraps

from flask_jwt_extended import get_jwt_identity


def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        current_user = get_jwt_identity()
        user = User.find_by_username(current_user)
        for role in user.roles:
            if 'admin' == role.name:
                return f(*args, **kwargs)
        return {'error': 'You do not have permission to access this resource!'}, 403

    return wrap


def coach_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        current_user = get_jwt_identity()
        user = User.find_by_username(current_user)
        for role in user.roles:
            if 'coach' == role.name:
                return f(*args, **kwargs)
        return {'error': 'You do not have permission to access this resource!'}, 403

    return wrap
