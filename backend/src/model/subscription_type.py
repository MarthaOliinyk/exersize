from src.app import db


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

    def return_one(self):
        return {
            'id': self.id,
            'name': self.name,
            'session_count': self.session_count,
            'duration': self.duration,
            'price': self.price,
        }

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'id': x.id,
                'name': x.name,
                'session_count': x.session_count,
                'duration': x.duration,
                'price': x.price,
                'course_id': x.course_id
            }

        return {'subscription_types': [to_json(s_type) for s_type in SubscriptionType.query.all()]}

    @classmethod
    def get_by_id(cls, sub_typeId):
        try:
            sub_type = cls.query.get(sub_typeId)
            return sub_type.return_one()
        except:
            return {'error': f'Subscription type with id={sub_typeId} does not exist!'}, 404

    @classmethod
    def delete_by_id(cls, sub_typeId):
        if cls.query.get(sub_typeId):
            cls.query.filter_by(id=sub_typeId).delete()
            db.session.commit()

            return {"message": f"Subscription type with id={sub_typeId} was successfully deleted"}
        else:
            return {'error': f'Subscription type with id={sub_typeId} does not exist!'}, 404
