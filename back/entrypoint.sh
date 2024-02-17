#!/bin/bash


# Create migrations if there are changes
echo "Checking for changes that require migrations..."
python manage.py makemigrations --dry-run | grep 'No changes detected' || {
  echo "Creating migrations..."
  python manage.py makemigrations app
  echo "<==================================>"
}
# Apply migrations
echo "Applying migrations..."
python manage.py migrate
echo "<==================================>"

# Create a superuser if it doesn't exist (customize this command as needed)
echo "Creating superuser..."
python manage.py create_superuser
echo "<==================================>"

# Add CSV
echo "Adding CSV..."
python manage.py import_csv app/static/cybersecurity_attacks.csv
echo "<==================================>"

# Start the server
echo "Starting server..."
python manage.py runserver 0.0.0.0:8000
echo "<==================================>"