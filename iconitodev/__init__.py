#iconitodev/__init__.py
#issue  dev           date       description
# na    Julio Conchas 03/16/2026 first creation
# na    Julio Conchas 03/16/2026 Add error_pages handlers blueprint
# na    Julio Conchas 03/16/2026 Add database setup to supabase

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os
from dotenv import load_dotenv

from iconitodev.core.view import core
from iconitodev.admin.view import admin
from iconitodev.error_pages.handlers import error_pages

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'iconito.iosecret'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True

########################
#### DATABASE SETUP ####
########################
app.config['SQLALCHEMY_DATABSE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

########################
#### LOGIN CONFIGS  ####
########################
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'


app.register_blueprint(core)
app.register_blueprint(admin)
app.register_blueprint(error_pages)