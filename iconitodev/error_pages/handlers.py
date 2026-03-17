#iconitodotcom/handlers.py
#issue  dev           date       description
# na    Julio Conchas 03/16/2026 first creation

from flask import Blueprint, render_template

error_pages = Blueprint('error_pages',__name__)

@error_pages.app_errorhandler(404)
def error_404(error):
    error_code="404"
    error_title="Page Not Found!"
    error_message="The page you're looking for doesn't exist or has been moved."
    return render_template('error_pages/error_pages.html',
                           error_code=error_code,
                           error_title=error_title
                           ,error_message=error_message), 404