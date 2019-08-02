import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension

basedir = os.path.abspath(os.path.dirname(__file__))

# Configure database
app = Flask(__name__)
app.config['SECRET_KEY'] = '\xd0\xa2\x19\xa4Z\xde\xf1\x94\x15sU4\xd1=\xcd\xfd2\xa4\x8b\xab\xceR\x8b\xb1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tetris.db')
app.config['DEBUG'] = True
db = SQLAlchemy(app)

# Configure authentication
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app)

# enable debug toolbar
toolbar = DebugToolbarExtension(app)

import Tetris.models
import Tetris.views
