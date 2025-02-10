#!/bin/bash

# Ensure the script has execution permissions
chmod +x build_files.sh

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Ensure pip is installed and updated inside the virtual environment
python3 -m ensurepip --default-pip
python3 -m pip install --upgrade pip

# Install dependencies from requirements.txt inside the virtual environment
pip install -r requirements.txt

python3 -m pip install Django==5.1


# Collect static files for Django
python3 manage.py collectstatic --noinput
