# Imports
from functools import wraps
from flask import request, abort

# Api Key Decorator
def requires_key(api_key):
	def decorator(view_function):
		@wraps(view_function)
		def decorated_function(*args, **kwargs):
			if request.args.get('key') and request.args.get('key') == api_key:
				return view_function(*args, **kwargs)
			else:
				abort(401)
		return decorated_function
	return decorator