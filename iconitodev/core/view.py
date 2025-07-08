#iconitodev/core/view.py
#issue dev           date       description
# 6    Julio Conchas 07/08/2025 Adding login view

from flask import render_template,request,Blueprint

core = Blueprint('core',__name__)

@core.route('/')
def index():
    return render_template('index.html')

@core.route('/login')
def login():
    return render_template('login.html')