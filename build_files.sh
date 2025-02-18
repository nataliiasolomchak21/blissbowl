#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python3 manage.py migrate

# Collect static files
python3 manage.py collectstatic --noinput

