#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Pull the latest code changes from your repository
git pull

# Install any new Python dependencies
pip install -r requirements.txt

# Gracefully restart the application server (e.g., using Gunicorn)
echo "Restarting the application server..."
kill -HUP `cat /path/to/gunicorn.pid`

# Optionally, perform database migrations if needed
# flask db upgrade

echo "Deployment complete."