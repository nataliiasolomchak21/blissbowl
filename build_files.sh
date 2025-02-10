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
python3 -m pip install dj-database-url==0.5.0
python3 -m pip psycopg2-binary==2.8.5
python3 -m pip cloudinary-storage==1.12.0
python3 -m pip ptyprocess==0.7.0
python3 -m pip pure_eval==0.2.3
python3 -m pip pycairo==1.27.0
python3 -m pip pycparser==2.22
python3 -m pip pydotplus==2.0.2
python3 -m pip Pygments==2.18.0
python3 -m pip python-dateutil==2.9.0.post0
python3 -m pip python-dotenv==1.0.1
python3 -m pip python-json-logger==2.0.7
python3 -m pip python3-openid==3.2.0
python3 -m pip pytz==2023.3.post1
python3 -m pip PyYAML==6.0.2
python3 -m pip pyzmq==26.2.0
python3 -m pip referencing==0.35.1
python3 -m pip requests==2.31.0
python3 -m pip requests-oauthlib==1.3.1
python3 -m pip rfc3339-validator==0.1.4
python3 -m pip rfc3986-validator==0.1.1
python3 -m pip rpds-py==0.20.0
python3 -m pip scikit-learn==1.5.2
python3 -m pip scipy==1.14.1
python3 -m pip Send2Trash==1.8.3
python3 -m pip sniffio==1.3.1
python3 -m pip soupsieve==2.6
python3 -m pip sqlparse==0.4.4
python3 -m pip stack-data==0.6.3
python3 -m pip stripe==7.7.0
python3 -m pip terminado==0.18.1
python3 -m pip threadpoolctl==3.5.0
python3 -m pip tinycss2==1.3.0
python3 -m pip tomli==2.0.1
python3 -m pip tornado==6.4.1
python3 -m pip traitlets==5.14.3
python3 -m pip types-python-dateutil==2.9.0.20240906
python3 -m pip typing_extensions==4.8.0
python3 -m pip tzdata==2024.1
python3 -m pip uri-template==1.3.0
python3 -m pip urllib3==1.26.18
python3 -m pip wcwidth==0.2.13
python3 -m pip webcolors==24.8.0
python3 -m pip webencodings==0.5.1
python3 -m pip websocket-client==1.8.0
python3 -m pip whitenoise==6.9.0


# Collect static files for Django
python3 manage.py collectstatic --noinput
