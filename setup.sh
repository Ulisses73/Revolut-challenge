#!/bin/bash

# Set environment variables
export APP_ENV=production
export FLASK_APP=app.py

# Configure database connection
export DATABASE_URI=your_database_uri

# Configure application-specific settings
export DEBUG=False
export LOG_LEVEL=info

# Install Python dependencies using a virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt