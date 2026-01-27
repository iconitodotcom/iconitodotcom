#iconitodev/admin/decorators.py
#issue  dev           date       description
# 14    Julio Conchas 01/26/2026 use session to prevent unauthorized user access restricted areas 

from functools import wraps 
from flask import session, redirect, url_for, request 

def login_required(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        if "user_id" not in session:
            return redirect(url_for('admin.login',next=request.path))
        return f(*args,**kwargs)
    return wrapper