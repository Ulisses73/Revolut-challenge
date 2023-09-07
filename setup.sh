#!/bin/bash

# Set environment variables
export APP_ENV=production
export FLASK_APP=app.py

# Configure database connection, fill the database_uri with the right one
export DATABASE_URI=database_uri

# Configure debug and log settings
export DEBUG=False
export LOG_LEVEL=info

# Install dependencies using a virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
