#!/bin/sh

python ./manage.py migrate

gunicorn catalogo_droids.wsgi -c gunicorn/gunicorn.conf.py
