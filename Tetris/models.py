from Tetris import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)

    def __repr__(self):
        return 'User: {}'.format(self.username)
