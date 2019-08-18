#!/usr/bin/env bash


echo "on wait for postgis"
set -x
sleep 3


#until python3 manage.py inspectdb ; do
#  >&2 echo "Postgres is unavailable - sleeping"
#  sleep 1
#done

>&2 echo "Postgres is up - executing command"
pwd
#cd backend
ls
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000