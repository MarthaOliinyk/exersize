from src.app import db


class UsersAppointments(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    appointment_id = db.Column(db.Integer(), db.ForeignKey('appointment.id', ondelete='CASCADE'))
