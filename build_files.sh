#!/bin/bash

# Ensure pip is installed and upgraded
python3 -m ensurepip --default-pip
python3 -m pip install --upgrade pip

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Collect static files for Django
python3 manage.py collectstatic --noinput
