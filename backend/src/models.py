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
    roles = db.relationship('Role', secondary='user_roles',
                            backref=db.backref('users', lazy='dynamic'))
    subscriptions = db.relationship('Subscription', backref='user', lazy=True)

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


class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(45), unique=True)

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()


class UserRoles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))


class RevokedTokens(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120))

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls, jti):
        return bool(cls.query.filter_by(jti=jti).first())


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    description = db.Column(db.String(200))
    tag = db.Column(db.String(45))
    subscription_type = db.relationship('SubscriptionType', backref='course', lazy=True)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'name': x.name,
                'description': x.description,
                'tag': x.tag
            }

        return {'courses': [to_json(course) for course in Course.query.all()]}

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

    @classmethod
    def get_id(cls, name):
        return cls.query.filter_by(name=name).first().id


class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    subscription_type_id = db.Column(db.Integer(), db.ForeignKey('subscription_type.id', ondelete='CASCADE'))

    def add(self):
        db.session.add(self)
        db.session.commit()


class SubscriptionType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    session_count = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    course_id = db.Column(db.Integer(), db.ForeignKey('course.id', ondelete='CASCADE'))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'name': x.name,
                'session_count': x.session_count,
                'duration': x.duration,
                'price': x.price,
                'course_id': x.course_id
            }

        return {'subscription_types': [to_json(s_type) for s_type in SubscriptionType.query.all()]}
