#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files for Django
python3 manage.py collectstatic --noinput
