#iconitodev/admin/view.py
#issue  dev           date       description
# na    Julio Conchas 07/08/2025 first creation
# na    Julio Conchas 12/27/2025 add Login View

from flask import render_template,request,Blueprint,redirect,url_for
from iconitodev.admin.forms import LoginForm

admin = Blueprint('admin',__name__)

@admin.route('/dashboard')
def dashboard():
    return render_template('admin/dashboard.html')


@admin.route('/login',methods=['GET','POST'])
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

    return render_template('admin/login.html',form=form)