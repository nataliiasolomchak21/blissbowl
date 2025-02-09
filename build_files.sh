#!/bin/bash

# Ensure pip is installed and upgraded
python3 -m pip install --upgrade pip

# Install dependencies from requirements.txt
python3 -m pip install -r requirements.txt

# Collect static files using the default python version
python3 manage.py collectstatic --no-input --clear
