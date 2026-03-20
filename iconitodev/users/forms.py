#iconitodev/users/forms.py
#issue  dev           date       description
# na    Julio Conchas 03/16/2026 first creatio

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional

from flask_login import current_user
from iconitodev.models import User


class LoginForm(FlaskForm):
    email    = EmailField   ('Email',    validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit   = SubmitField  ('Login')


class RegistrationForm(FlaskForm):
    username         = StringField  ('Username', validators=[DataRequired(), Length(min=3, max=80)])
    email            = EmailField   ('Email',    validators=[DataRequired(), Email()])
    password         = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit           = SubmitField  ('Register')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')
    
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has been registered already!')


class UpdateProfileForm(FlaskForm):
    username        = StringField('Username', validators=[DataRequired(), Length(min=3, max=80)])
    email           = EmailField ('Email',    validators=[DataRequired(), Email()])
    current_password = PasswordField('Current Password', validators=[Optional()])
    new_password    = PasswordField ('New Password',     validators=[Optional(), Length(min=6)])
    confirm_password = PasswordField('Confirm New Password',
                           validators=[EqualTo('new_password', message='Passwords must match')])
    profile_picture = FileField('Profile Picture',validators=[FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
    submit          = SubmitField('Update Profile')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')
    
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has been registered already!')