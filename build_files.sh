#!/bin/bash

# Exit on error
set -e

# Set up virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip to the latest version
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run database migrations
python manage.py migrate --noinput

# Other commands (if needed)
# e.g., python manage.py test

# Deactivate virtual environment
deactivate
