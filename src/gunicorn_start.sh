#!/bin/bash

NAME="menu-app"
BIND=0.0.0.0:5000
USER=mono
GROUP=mono
NUM_WORKERS=4
WSGI_MODULE=wsgi

exec pipenv run gunicorn ${WSGI_MODULE}:app \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --log-level=error \
  --bind=$BIND \
  --preload
