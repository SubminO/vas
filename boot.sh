#!/bin/sh

exec gunicorn -b :8000 -w 5 --access-logfile - --error-logfile - www.wsgi:application
