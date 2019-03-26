# Imports
import json
from functools import wraps
from auth import requires_key
from flask_socketio import SocketIO, emit, send
from flask import Flask, Response, request, jsonify, abort

# Initiate flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'fjnk42f347y78fq2h4f83!@#'
api_key = 'ZaxtfTpNj0mV3fZ0GlWdktKj8SpiBS0gRBXVNIMUR5NZms1w3K'

# Wrap socketio around flask app
socketio = SocketIO(app)

@app.route('/')
@requires_key(api_key)
def index():
    return Response('', status=200, mimetype='application/json')

@app.route('/receive', methods=['POST'])
@requires_key(api_key)
def receive_notification_from_source():
	try:
		data = request.get_json()
		# Send notification to browser
		socketio.emit('notification', {'data': data['message']})
		return Response("{'message':'Success'}", status=200, mimetype='application/json')
	except Exception as e:
		print(e)
		return Response("{'message':'Failed'}", status=400, mimetype='application/json')

# Socket.io event handling

if __name__ == '__main__':
    socketio.run(app)