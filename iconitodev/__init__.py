#iconitodev/__init__.py

from flask import Flask 
from iconitodev.core.view import core

app = Flask(__name__)
app.register_blueprint(core)