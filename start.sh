#!/bin/bash

python3 manage.py migrate
python3 manage.py seed
heroku config:set DISABLE_COLLECTSTATIC=1
python3 manage.py collectstatic
gunicorn --bind 0.0.0.0:8000 m2a.wsgi
