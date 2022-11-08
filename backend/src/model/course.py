from src.app import db
from flask import jsonify
from sqlalchemy import or_


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    tag = db.Column(db.String(30), nullable=False)
    subscription_types = db.relationship('SubscriptionType', backref='course', lazy=True)
    users = db.relationship('User', secondary='users_courses', viewonly=True)
    schedules = db.relationship('Schedule', backref='course', lazy=True)

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
    def return_one(cls, course_id):
        def to_json(x):
            return {
                'name': x.name,
                'description': x.description,
                'tag': x.tag
            }

        return {'course': [to_json(cls.query.filter_by(id=course_id).first())]}

    @classmethod
    def delete_by_id(cls, course_id):
        try:
            cls.query.filter_by(id=course_id).delete()
            db.session.commit()

            return jsonify({
                'message': f'course {course_id} deleted'
            })
        except:
            return jsonify({
                'message': 'Something went wrong'
            })

    @classmethod
    def get_id(cls, name):
        return cls.query.filter_by(name=name).first().id

    @classmethod
    def update_by_id(cls, course_id, data):
        try:
            sub_type = cls.query.filter_by(id=course_id).first()
            sub_type.name = data['name']
            sub_type.description = data['description']
            sub_type.tag = data['tag']
            db.session.commit()
            return jsonify({
                'message': f'course {course_id} updated'
            })
        except:
            return jsonify({
                'message': 'Something went wrong'
            })

    @classmethod
    def search_courses(cls, text):
        def to_json(x):
            return {
                'name': x.name,
                'description': x.description,
                'tag': x.tag
            }

        query = cls.query.filter(or_(Course.name.like(f'%{text}%'), Course.description.like(f'%{text}%'))).all()
        return {'courses': [to_json(course) for course in query]}
