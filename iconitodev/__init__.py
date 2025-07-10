#iconitodev/__init__.py

from flask import Flask 
from iconitodev.core.view import core
from iconitodev.admin.view import admin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'iconito.iosecret'

app.register_blueprint(core)
app.register_blueprint(admin)