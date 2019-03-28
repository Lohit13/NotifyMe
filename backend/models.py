from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Namespace(db.Model):
	__tablename__ = 'namespace'

	key = db.Column(db.Integer, primary_key=True)

	def __init__(self, key):
		self.key = key

	def __repr__(self):
		return self.key

	def serialize(self):
		return {
			'key': self.key
		}