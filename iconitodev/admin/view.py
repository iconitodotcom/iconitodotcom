#iconitodev/admin/view.py
#issue  dev           date       description
# na    Julio Conchas 07/08/2025 first creation

from flask import render_template,request,Blueprint

admin = Blueprint('admin',__name__)

@admin.route('/dashboard')
def dashboard():
    return render_template('admin/dashboard.html')