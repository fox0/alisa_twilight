#!/usr/bin/env bash

virtualenv --no-site-packages --never-download --python=python3 venv
. venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
