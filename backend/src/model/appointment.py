from src.app import db
from flask import jsonify


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime, nullable=False)
    schedule_id = db.Column(db.Integer(), db.ForeignKey('schedule.id', ondelete='CASCADE'))
    users = db.relationship('User', secondary='users_appointments', viewonly=True)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def to_json(x):
        return {
            'id': x.id,
            'time': x.time,
            'schedule_id': x.schedule_id
        }

    @classmethod
    def get_by_id(cls, appointment_id):
        return cls.query.filter_by(id=appointment_id).first()

    @classmethod
    def get_by_schedule_id(cls, schedule_id):
        return cls.query.filter_by(schedule_id=schedule_id).all()
