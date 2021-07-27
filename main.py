from flask import Blueprint,render_template
#from .models import db
from flask_login import login_required, current_user

auth = Blueprint('auth', __name__)
main = Blueprint('main', __name__)#Creting Blueprint

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)