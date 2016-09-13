from flask import Blueprint, render_template
#from flask.ext.cors import CORS, cross_origin
from flask import request

#from app import db

# # Import module forms
# from app.mod_auth.forms import LoginForm

# # Import module models (i.e. User)
# from app.mod_auth.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_store = Blueprint('store', __name__, url_prefix='/store')

# Set the route and accepted methods

# TODO: get CORS to work
# TODO merge bad & good routes

@mod_store.route('/good', methods=['GET'])
#@cross_origin(origin='localhost')
def good():
	store('good')
	return ''

@mod_store.route('/bad', methods=['GET'])
#@cross_origin(origin='localhost')
def bad():
	store('bad')
	return ''

def store(label):
	url = request.args['url']
	date = request.args['date']
	title = request.args['title']
	summary = request.args['summary']
	with open(label + 's.txt', 'a') as fo:
		fo.write(date)
		fo.write(';')
		fo.write(url)
		fo.write(';')
		fo.write('"' + title.replace('"', '""') + '"')
		fo.write(';')
		fo.write('"' + summary.replace('"', '""') + '"')
		fo.write('\n')