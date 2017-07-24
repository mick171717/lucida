from flask import *
from Database import database
from AccessManagement import login_required
from ThriftClient import thrift_client
from QueryClassifier import query_classifier
from Utilities import log, check_image_extension
from copy import deepcopy
from Config import WFList
import Config
import os
import json

infer = Blueprint('infer', __name__, template_folder='templates')

@login_required
def generic_infer_route(form, upload_file):
	options = {}
	try:
		# Deal with POST requests.
		if request.method == 'POST':
			if not upload_file is None and upload_file.filename != '':
				check_image_extension(upload_file)
			# Classify the query.
			speech_input = form['speech_input'] if 'speech_input' in form \
				else ''
			print '@@@@@@@@@@', speech_input
			image_input = [upload_file.read()] if upload_file else []
			lucida_id = session['username']
			# Check if context is saved for Lucida user
			# If not, classify query, otherwise restore session
			if lucida_id not in Config.SESSION:
				workflow_needed = query_classifier.predict(speech_input, upload_file)
				text_input = [speech_input]
				workflow = deepcopy(WFList[workflow_needed])
				options['result'] = thrift_client.infer(lucida_id, workflow, text_input, image_input)			
			else:
				if 'workflow' in Config.SESSION[lucida_id]:
					workflow = Config.SESSION[lucida_id]['workflow']
					text_input = Config.SESSION[lucida_id]['resulttext']
					text_input.insert(0, speech_input)
					options['result'] = thrift_client.infer(lucida_id, workflow, text_input, image_input)
				else:
					workflow_needed = query_classifier.predict(speech_input, upload_file)
					text_input = Config.SESSION[lucida_id]['resulttext']
					text_input.insert(0, speech_input)
					workflow = deepcopy(WFList[workflow_needed])
					options['result'] = thrift_client.infer(lucida_id, workflow, text_input, image_input)		
			log('Result ' + options['result'])
			'''
			# Check if Calendar service is needed.
			# If so, JavaScript needs to receive the parsed dates.
			if services_needed.has_service('CA'):
				options['dates'] = options['result']
				options['result'] = None
			'''
	except Exception as e:
		log(e)
		options['errno'] = 500
		options['error'] = str(e)
		if 'code' in e and re.match("^4\d\d$", str(e.code)):
			options['errno'] = e.code
		if str(e) == 'TSocket read 0 bytes':
			options['error'] = 'Back-end service encountered a problem'
		if str(e).startswith('Could not connect to'):
			options['error'] = 'Back-end service is not running'
	return options

@infer.route('/infer', methods=['GET', 'POST'])
@login_required
def infer_route():
	options = {}
	if os.environ.get('ASR_ADDR_PORT'):
		options['asr_addr_port'] = os.environ.get('ASR_ADDR_PORT')
	else:
		options['asr_addr_port'] = 'ws://localhost:8081'
	if request.method == 'POST':
		options = generic_infer_route(request.form, request.files['file'] if 'file' in request.files else None)
	return render_template('infer.html', **options)

@infer.route('/api/infer', methods=['POST'])
def api_infer_route():
	session['username'] = database.get_username(request.form['interface'], request.form['username'])
	if session['username'] == None:
		abort (403)

	session['logged_in'] = True
	print '@@@@@@@@', session['username']

	options = generic_infer_route(request.form, request.files['file'] if 'file' in request.files else None)

        if 'errno' in options:
            return json.dumps(options), options['errno']
	return json.dumps(options), 200
