#!/bin/bash

#!/bin/bash

# Install required system libraries
apt-get update && apt-get install -y libffi-dev libcairo2-dev libpq-dev gcc

# Ensure pip is installed and upgraded
python3 -m ensurepip --default-pip
python3 -m pip install --upgrade pip

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

python3 -m pip install Django==5.1
python3 -m pip install dj-database-url==0.5.0
python3 -m pip install psycopg2-binary==2.8.5
python3 -m pip install cloudinary==1.36.0
python3 -m pip install django-allauth==65.3.1
python3 -m pip install dj3-cloudinary-storage==0.0.6
python3 -m pip install django-crispy-forms==1.12.0


# Collect static files for Django
python3 manage.py collectstatic --noinput
