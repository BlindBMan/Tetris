from flask import render_template, url_for, request, redirect, flash, abort

from Tetris import app, db, login_manager
from flask_login import current_user, logout_user, login_user, login_required
from .models import User, Game
from .forms import SignupForm, LoginForm


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
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    password=form.password.data,
                    email=form.email.data)
        db.session.add(user)
        db.session.commit()
        flash('Welcome {}! Please log in'.format(user.username))
        return redirect(url_for('login'))
    return  render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_username(form.username.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, form.remember_me.data)
            flash('Logged in as {}. Welcome back!'.format(user.username))
            return redirect(request.args.get('next') or url_for('index'))
        flash('Incorrect username or password')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<username>')
def user(username):
    pass
