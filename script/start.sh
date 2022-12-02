#!/bin/bash

if [ $# -eq 0 ]; then
	echo "Usage: start.sh [PROCESS_TYPE](server)"
	exit 1
fi

PROCESS_TYPE=$1

if [ "$PROCESS_TYPE" = "server" ]; then
	if [ "$DJANGO_DEBUG" = "true" ]; then
		gunicorn \
			--reload \
			--bind 0.0.0.0:8000 \
			--workers 2 \
			--log-level DEBUG \
			--access-logfile "-" \
			--error-logfile "-" \
			forumkowan.wsgi

	else
		gunicorn \
			--bind 0.0.0.0:8000 \
			--workers 2 \
			--log-level DEBUG \
			--access-logfile "-" \
			--error-logfile "-" \
			forumkowan.wsgi
	fi
fi
