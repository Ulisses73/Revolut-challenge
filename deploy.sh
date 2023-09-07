#!/bin/bash

# Virtual environment
source venv/bin/activate

# Pull the latest changes from repository
git pull

# Install any new dependencies
pip install -r requirements.txt

# Gracefully restart the application server
echo "Restarting the application server"
kill -HUP `cat /path/to/gunicorn.pid`

# Perform database migrations if needed
# flask db upgrade

echo "Deployment complete."
