from app import db


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
