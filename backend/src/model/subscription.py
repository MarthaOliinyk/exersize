from src.app import db


class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    session_number = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    subscription_type_id = db.Column(db.Integer(), db.ForeignKey('subscription_type.id', ondelete='CASCADE'))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def return_one(self):
        return {
            'id': self.id,
            'start': self.start,
            'end': self.end,
            'session_number': self.session_number,
            'user_id': self.user_id,
            'subscription_type_id': self.subscription_type_id
        }

    @classmethod
    def get_by_id(cls, subId):
        try:
            sub = cls.query.get(subId)
            return sub.return_one()
        except:
            return {'error': f'Subscription with id={subId} does not exist!'}, 404

    @classmethod
    def delete_by_id(cls, subId):
        if cls.query.get(subId):
            cls.query.filter_by(id=subId).delete()
            db.session.commit()

            return {"message": f"Subscription with id={subId} was successfully deleted"}
        else:
            return {'error': f'Subscription with id={subId} does not exist!'}, 404
