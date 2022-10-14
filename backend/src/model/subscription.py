from src.app import db


class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    subscription_type_id = db.Column(db.Integer(), db.ForeignKey('subscription_type.id', ondelete='CASCADE'))

    def add(self):
        db.session.add(self)
        db.session.commit()
