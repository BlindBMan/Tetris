from flask import render_template, url_for, request, redirect, flash, abort

from Tetris import app, db, login_manager
from .models import User, Game


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
