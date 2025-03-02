#!/bin/bash

# Ensure pip is installed (it's usually installed with Python 3)
python3 -m ensurepip --upgrade

# Install dependencies from requirements.txt
pip3 install -r requirements.txt

# Run collectstatic to gather static files
python3 manage.py collectstatic --noinput
