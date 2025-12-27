#iconitodev/core/view.py
#issue dev           date       description
# 6    Julio Conchas 07/08/2025 Adding login view
# na   Julio Conchas 12/27/2025 remove login view, moved to admin app

from flask import render_template,request,Blueprint,redirect,url_for
from iconitodev.core.forms import LoginForm

core = Blueprint('core',__name__)

@core.route('/')
def index():
    return render_template('index.html')
