from app import db


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    participants = db.Column(db.Integer, nullable=False)
    course_id = db.Column(db.Integer(), db.ForeignKey('course.id', ondelete='CASCADE'))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def return_one(self):
        return {
            'start': self.start,
            'end': self.end,
            'participants': self.participants
        }

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'start': x.start,
                'end': x.end,
                'participants': x.participants
            }

        return {'schedules': [to_json(schedule) for schedule in Schedule.query.all()]}
