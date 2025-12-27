#iconitodev/admin/forms.py
#issue dev           date       description
# na   Julio Conchas 12/23/2025 first creation

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    user = StringField("Username",validators=[DataRequired()]) 
    pwd = PasswordField("Password",validators=[DataRequired()])