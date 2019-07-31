from Tetris import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(30), unique=True)
    games = db.relationship('Game', backref='user', lazy='dynamic')
    password_hash = db.Column(db.String)

    @property
    def password(self):
        raise AttributeError('password field is read-only ')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'User: {}'.format(self.username)


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return 'Game for user {} with score {}'.format(self.user_id, self.score)
