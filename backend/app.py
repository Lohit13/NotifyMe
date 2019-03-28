# Imports
import json, os
from .auth import requires_key
from flask_socketio import SocketIO, emit, send
from flask import Flask, Response, request, jsonify, abort
from .models import *

# Initiate flask app
app = Flask(__name__)

# Load app config
app.config.from_pyfile('config/config.cfg')
if len(os.environ['NOTIFICATION_ENV']) > 0:
	app.config.from_pyfile('config/config-' + os.environ['NOTIFICATION_ENV'] + '.cfg')

print('Environment : ', os.environ['NOTIFICATION_ENV'])

# Init DB
db.init_app(app)

# API key for testing
api_key = 'ZaxtfTpNj0mV3fZ0GlWdktKj8SpiBS0gRBXVNIMUR5NZms1w3K'

# Wrap socketio around flask app
socketio = SocketIO(app)

# Socket connect endpoint
@app.route('/', methods=['GET'])
@requires_key(api_key)
def index():
    return Response('', status=200, mimetype='application/json')

# Notification receiving endpoint from source
@app.route('/receive', methods=['POST'])
@requires_key(api_key)
def receive_notification_from_source():
	try:
		data = request.get_json()
		# Send notification to destination
		socketio.emit('notification', {'data': data['message']})
		return Response("{'message':'Success'}", status=200, mimetype='application/json')
	except Exception as e:
		print(e)
		return Response("{'message':'Failed'}", status=400, mimetype='application/json')

if __name__=='__main__':
	socketio.run(app)