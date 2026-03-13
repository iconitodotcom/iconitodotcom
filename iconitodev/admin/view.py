#iconitodev/admin/view.py
#issue  dev           date       description
# na    Julio Conchas 07/08/2025 first creation
# na    Julio Conchas 12/27/2025 add Login View
# 12    Julio Conchas 01/25/2026 add connection to db, modify login to get auth from db
# 14    Julio Conchas 01/26/2026 use session to prevent unauthorized user access restricted areas 

from flask import render_template,request,Blueprint,redirect,url_for,session
from iconitodev.admin.forms import LoginForm
from iconitodev.admin.db import *
from iconitodev.admin.decorators import login_required

admin = Blueprint('admin',__name__)

@admin.route('/dashboard')
@login_required
def dashboard():
    return render_template('admin/dashboard.html')


@admin.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        print(f'form data = {form.data}')
        # DB call here 
        auth = login_user(email=form.data['email'],password=form.data['pwd'])
        print(f'Aauth = {auth}')
        print(f'Aauth = {auth[RESPONSE_USER].id}')
        if auth[RESPONSE_SUCCESS]:
            session["user_id"] = auth[RESPONSE_USER].id
            session["role"] = DB_ADMIN_ROLE if is_admin(auth[RESPONSE_USER].id) else DB_USER_ROLE
            return redirect(url_for('admin.dashboard'))
        else:
            render_template('admin/login.html',error="Auth error")

    return render_template('admin/login.html',form=form)