from flask import Blueprint, render_template

from app import db

# # Import module forms
# from app.mod_auth.forms import LoginForm

# # Import module models (i.e. User)
from app.modules.user.models import User, 
from app.modules.user.forms import LoginForm, RegisterForm, EditProfileForm

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_user = Blueprint('user', __name__, url_prefix='/users')
TMP_PREFIX = 'user/'

# Set the route and accepted methods
@mod_user.route('/login', methods=['GET', 'POST'])
def login():
	if :

	else:
	return render_template(TMP_PREFIX + 'login.html', form=form)

@mod_user.route('/register', methods=['GET', 'POST'])
def register():
	return render_template(TMP_PREFIX + 'register.html', form=form)

@mod_user.route('/<str:username>/view')
def profile_view():
	return render_template(TMP_PREFIX + 'profile_view.html')

mod_user.route('/<str:username>/edit')
def profile_edit():
	"""Edit either user's own profile, or edit someone else's profile by admin"""
	return render_template(TMP_PREFIX + 'profile_edit.html', form=form)

@mod_user.route('/list')
@mod_user.route('/list/<int:pageid>')
def user_list():
	"""User list, optionaly with edit link for admin"""
	return render_template(TMP_PREFIX + 'userlist.html', userlist=userlist, pageid=pageid)