from app import db
from flask import jsonify
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
    roles = db.relationship('Role', secondary='users_roles',
                            backref=db.backref('user', lazy='dynamic'))
    subscriptions = db.relationship('Subscription', backref='user', lazy=True)
    courses = db.relationship('Course', secondary='users_courses',
                              backref=db.backref('user', lazy='dynamic'))

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
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def return_all(cls):

        def to_json(x):
            return {
                'username': x.username,
                'password': x.password,
                'email': x.email,
                'fullname': x.fullname,
                'age': x.age
            }

        return {'users': [to_json(user) for user in User.query.all()]}

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()

            return jsonify({
                "message": f"{num_rows_deleted} row(s) deleted"
            })
        except:
            return jsonify({
                "message": "Something went wrong"
            })

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash_):
        return sha256.verify(password, hash_)
