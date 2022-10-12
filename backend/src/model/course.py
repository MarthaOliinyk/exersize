from app import db
from flask import jsonify


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    description = db.Column(db.String(200))
    tag = db.Column(db.String(45))
    subscription_type = db.relationship('SubscriptionType', backref='course', lazy=True)
    users = db.relationship('User', secondary='users_courses', viewonly=True)

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
