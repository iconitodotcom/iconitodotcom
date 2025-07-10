#iconitodev/core/forms.py
#issue dev           date       description
# na   Julio Conchas 07/08/2025 first creation

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    user = StringField("Username",validators=[DataRequired()]) 
    pwd = PasswordField("Password",validators=[DataRequired()])