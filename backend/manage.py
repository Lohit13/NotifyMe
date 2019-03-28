# Imports
import click
from models import db
from app import app, socketio
from flask_migrate import Migrate, MigrateCommand, upgrade, init

from pprint import pprint

migrate = Migrate(app, db)

with app.app_context():
	try:
		init()
	except:
		pass
	upgrade(directory='./migrations')

def run():
	"Starts the flask app wrapped in SocketIO"
	socketio.run(app)

if __name__=='__main__':
	pass