from flask import render_template, url_for, request, redirect, flash, abort

from Tetris import app, db, login_manager
from .models import User, Game
from flask_login import current_user, logout_user, login_user, login_required


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/play')
def play():
    return render_template('play.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return  render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<username>')
def user(username):
    pass
