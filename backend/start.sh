#!/bin/bash

# Start up script for Notification Backend
environment=development

while [ "$1" != "" ]; do
	case $1 in
		-e | --env )	shift
						environment=$1
						;;
		-h | --help)	echo "Usage: ./start.sh -e <environment>"
						exit
						;;
	esac
	shift
done

if [ $# -lt 1 ]; then
	echo "Environment not given. Defaulting to \`development\`"
fi

export NOTIFICATION_ENV=$environment
export FLASK_APP=app.py
flask run