#iconitodev/admin/db.py
#issue  dev           date       description
# 12    Julio Conchas 01/25/2026 first creation, integrate db to project

from supabase import create_client
from gotrue.errors import AuthApiError
from dotenv import load_dotenv
import os

load_dotenv()

RESPONSE_SUCCESS = 'success'
RESPONSE_USER = 'user'
RESPONSE_SESSION = 'session'
RESPONSE_ERROR = 'error'

supabase_anon = create_client(
    supabase_url=os.getenv("SUPABASE_URL"),
    supabase_key=os.getenv("SUPABASE_ANON_KEY")
)

supabase_admin = create_client(
    supabase_url=os.getenv("SUPABASE_URL"),
    supabase_key=os.getenv("SUPABASE_SERVICE_ROLE_KEY")
)
def login_user(email,password):
    login_response = {}

    try:
        response = supabase_anon.auth.sign_in_with_password({
            "email": email,
            "password" : password
        })
        login_response[RESPONSE_SUCCESS] = True 
        login_response[RESPONSE_USER] = response.user 
        login_response[RESPONSE_SESSION] = response.session

    except AuthApiError as e:
        login_response[RESPONSE_SUCCESS] = False 
        login_response[RESPONSE_ERROR] = "Invalid email or passowrd"
    except Exception as e:
        login_response[RESPONSE_SUCCESS] = False 
        login_response[RESPONSE_ERROR] = "Authentication service unavailable"
    return login_response