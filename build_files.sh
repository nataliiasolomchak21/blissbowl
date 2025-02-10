# build_files.sh

# Ensure pip is installed
python3 -m ensurepip --default-pip

# Upgrade pip
python3 -m pip install --upgrade pip

# Install dependencies
python3 -m pip install -r requirements.txt

# Collect static files for Django
python3 manage.py collectstatic --noinput
