from src.app import db
from passlib.hash import pbkdf2_sha256 as sha256
from sqlalchemy import func
from sqlalchemy import DateTime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    fullname = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    registrationDate = db.Column(DateTime(timezone=True), server_default=func.now())
    subscriptions = db.relationship('Subscription', backref='user', lazy=True)
    roles = db.relationship('Role', secondary='users_roles',
                            backref=db.backref('user', lazy='dynamic'))
    courses = db.relationship('Course', secondary='users_courses',
                              backref=db.backref('user', lazy='dynamic'))

    def to_json(self):
        return {
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'fullname': self.fullname,
            'age': self.age
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, userId):
        return cls.query.filter_by(id=userId).first()

    @classmethod
    def get_all(cls):
        return {'users': [cls.to_json(user) for user in User.query.all()]}

    @classmethod
    def get_by_id(cls, userId):
        try:
            user = User.query.filter_by(id=userId).first()
            return cls.to_json(user)
        except AttributeError:
            return {'error': f'User with {userId} does not exist!'}, 404

    @classmethod
    def delete_by_id(cls, userId):
        try:
            user = cls.query.filter_by(id=userId).delete()
            db.session.commit()

            return {"message": f"User with id={userId} was successfully deleted"}
        except AttributeError:
            return {'error': f'User with {userId} does not exist!'}, 404

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash_):
        return sha256.verify(password, hash_)
