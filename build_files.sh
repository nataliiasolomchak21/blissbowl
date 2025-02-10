#!/bin/bash

# Ensure pip is installed and upgraded
python3 -m ensurepip --default-pip
python3 -m pip install --upgrade pip

# Check Python version
echo "Python version:"
python3 --version

# Check pip version
echo "Pip version:"
python3 -m pip --version

# Install dependencies
python3 -m pip install --no-cache-dir -r requirements.txt

python3 -m pip install Django==5.1


# Debugging: Check if Django is installed
echo "Installed packages:"
python3 -m pip list

# Collect static files
python3 manage.py collectstatic --noinput
