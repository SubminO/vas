#!/bin/sh
#source ../venv/bin/activate
#while true; do
#    flask db upgrade
#    if [[ "$?" == "0" ]]; then
#        break
#    fi
#    echo Upgrade command failed, retrying in 5 secs...
#    sleep 5
#done
python manage.py collectstatic --noinput
python manage.py migrate
exec gunicorn -b :8000 -w 5 --access-logfile - --error-logfile - www.wsgi:application