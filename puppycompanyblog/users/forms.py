from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from puppycompanyblog import User

class LoginForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    username = StringField('Username: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataREquired(), EqualTo('pass_corfirm'), message="Passwords must match"])
    pass_confirm = PasswordField('Confirm Password: ', validators=[DataRequired()])


def check_email(self, field):
    if User.query.filter_by(email=field.data).first():
        raise ValidationError('Your email is already in use. Please choose another.')

def check_username(self, field):
    if User.query.filter_by(email=field.data).first():
        raise ValidationError('Your username is already in use. Please choose another.')