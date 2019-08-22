#!/usr/bin/env bash

set -x

python3 manage.py wait_database
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000