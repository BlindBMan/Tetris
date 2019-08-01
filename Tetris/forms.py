from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, ValidationError, Length, Regexp, EqualTo, Email
from .models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(5,20),
                                                    Regexp('^[A-Za-z0-9]{3,}$',
                                                           message='User names consist of numbers, '
                                                                   'letters and underscores')
                                                    ])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 30),
                                                      EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])

    def validate_email(self, email_field):
        if User.query.filter_by(email=email_field.data).first():
            raise ValidationError('Email already registered')

    def validate_username(self, username_field):
        if User.query.filter_by(username=username_field.data).first():
            raise ValidationError('Its 2019, be more creative')
