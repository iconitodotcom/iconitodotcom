#iconitodev/core/view.py
#issue dev           date       description
# 6    Julio Conchas 07/08/2025 Adding login view

from flask import render_template,request,Blueprint,redirect,url_for
from iconitodev.core.forms import LoginForm

core = Blueprint('core',__name__)

@core.route('/')
def index():
    return render_template('index.html')

@core.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        print(f'form data = {form.data}')
        # DB call here 
        if form.data['user'] == 'jconchas' and form.data['pwd'] == 'pedos':
            # redirect to admin
            return redirect(url_for('admin.dashboard'))
        else:
            print("Not the right credentials")

    return render_template('login.html',form=form)