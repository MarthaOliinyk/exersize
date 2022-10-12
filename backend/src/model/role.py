from app import db


class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(45), unique=True)

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
