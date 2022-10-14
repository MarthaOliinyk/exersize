from src.app import db


class UsersCourses(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    course_id = db.Column(db.Integer(), db.ForeignKey('course.id', ondelete='CASCADE'))
