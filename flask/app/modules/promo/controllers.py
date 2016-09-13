from flask import Blueprint, render_template

from app import db

# # Import module forms
# from app.mod_auth.forms import LoginForm

# # Import module models (i.e. User)
# from app.mod_auth.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_promo = Blueprint('promo', __name__, url_prefix='/promo')

# Set the route and accepted methods
@mod_promo.route('/')
def index():
	return render_template('promo/index.html')