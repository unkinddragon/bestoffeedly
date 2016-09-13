from flask import Blueprint
from flask import request

mod_ml = Blueprint('ml', __name__, url_prefix='/ml')

# Set the route and accepted methods

@mod_ml.route('/add_example', methods=['GET'])
def add_example():
	label = request.args['label']
	data = []
	keys = ['url', 'date', 'title', 'summary'] # should be selected on user/project basis
	for key in keys:
		data.append(request.args[key])
	store(label, data)
	return ''

def store(label, data):
	with open('examples.txt', 'a') as fo:
		sep = ';'
		newline = '\n'
		output = label
		for value in data:
			output += sep + escape_text(value)
		print(output, file=fo, end=newline)

def escape_text(text):
	return '"' + text.replace('"', '""') + '"'