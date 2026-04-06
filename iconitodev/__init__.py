#iconitodev/__init__.py
#issue  dev           date       description
# na    Julio Conchas 03/16/2026 first creation
# na    Julio Conchas 03/16/2026 Add error_pages handlers blueprint
# na    Julio Conchas 03/16/2026 Add database setup to supabase
# na    Julio Conchas 03/19/2026 Adding users blueprint

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os
from dotenv import load_dotenv



load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'iconito.iosecret'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True

########################
#### DATABASE SETUP ####
########################
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['TIGRIS_BASE_URL'] = os.getenv('BUCKET_NAME')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

########################
#### LOGIN CONFIGS  ####
########################
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

##################################
#### Blueprints registration  ####
##################################

from iconitodev.core.view import core
from iconitodev.admin.view import admin
from iconitodev.users.views import users
from iconitodev.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(admin)
app.register_blueprint(users)
app.register_blueprint(error_pages)

##############
# app config #
##############
@app.context_processor
def inject_globals():
    return {
        'MEDIA_URL': app.config.get('TIGRIS_BASE_URL')
    }
