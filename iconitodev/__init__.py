#iconitodev/__init__.py

from flask import Flask 
from iconitodev.core.view import core
from iconitodev.admin.view import admin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'iconito.iosecret'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True

app.register_blueprint(core)
app.register_blueprint(admin)