from app import db, loginmanager
from werkzeug.security import generate_password_hash, check_password_hash

@loginmanager.user_loader
def user_loader(id):
    return User.query.get(int(id))

from flask_login import UserMixin
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    quiz1 = db.Column(db.Integer)
    quizSt = db.Column(db.Integer)
    quizAr = db.Column(db.Integer)
    quizTr = db.Column(db.Integer)
    quizQu = db.Column(db.Integer)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
