from src.app import db
from src.model.course import Course


class SubscriptionType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    session_count = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    course_id = db.Column(db.Integer(), db.ForeignKey('course.id', ondelete='CASCADE'))
    subscriptions = db.relationship('Subscription', backref='subscription_type', lazy=True)

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
            'course_id': self.course_id
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
    def delete_by_id(cls, sub_typeid):
        if cls.query.get(sub_typeid):
            cls.query.filter_by(id=sub_typeid).delete()
            db.session.commit()
            return {'message': f'Subscription type with id={sub_typeid} was successfully deleted'}
        else:
            return {'error': f'Subscription type with id={sub_typeid} does not exist!'}, 404

    @classmethod
    def get_filtered_subsciption_types(cls, data):
        filtered_sub_types = db.session.query(SubscriptionType).join(Course).filter(Course.tag == data['tag']) \
            .filter(SubscriptionType.duration == data['duration']) \
            .filter(SubscriptionType.price == data['price']).all()

        def to_json(x):
            return Course.return_one(x.course_id), \
                   {
                       'subscription_type': {'id': x.id,
                                             'name': x.name,
                                             'session_count': x.session_count,
                                             'duration': x.duration,
                                             'price': x.price,
                                             'course_id': x.course_id}
                   }

        return {'filtered subscription types': [to_json(s_type) for s_type in filtered_sub_types]}
