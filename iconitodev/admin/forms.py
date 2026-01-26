#iconitodev/admin/forms.py
#issue dev           date       description
# na   Julio Conchas 12/23/2025 first creation
# 12   Julio Conchas 01/25/2026 add connection to db so change user field to email

from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = EmailField("Email",validators=[DataRequired()]) 
    pwd = PasswordField("Password",validators=[DataRequired()])