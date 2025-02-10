#!/bin/bash

# Ensure the script has execution permissions
chmod +x build_files.sh

# Ensure pip is installed and updated
python3 -m ensurepip --default-pip
python3 -m pip install --upgrade pip

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Check Python version
echo "Python version:"
python3 --version

# Check pip version
echo "Pip version:"
python3 -m pip --version

python3 -m pip install Django==5.1
python3 -m pip install dj-database-url==0.5.0
python3 -m pip install psycopg2-binary==2.8.5
python3 -m pip install dj3-cloudinary-storage==0.0.6


# Collect static files
python3 manage.py collectstatic --noinput
