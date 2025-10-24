#!/bin/bash

# Install Python dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Create static directory
echo "Creating static directories..."
mkdir -p static
mkdir -p staticfiles

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "Build completed successfully!"