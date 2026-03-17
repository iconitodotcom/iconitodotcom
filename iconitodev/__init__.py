#iconitodev/__init__.py
#issue  dev           date       description
# na    Julio Conchas 03/16/2026 first creation
# na    Julio Conchas 03/16/2026 Add error_pages handlers blueprint

from flask import Flask 
from iconitodev.core.view import core
from iconitodev.admin.view import admin
from iconitodev.error_pages.handlers import error_pages

app = Flask(__name__)
app.config['SECRET_KEY'] = 'iconito.iosecret'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True

app.register_blueprint(core)
app.register_blueprint(admin)
app.register_blueprint(error_pages)