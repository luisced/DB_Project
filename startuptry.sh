#!/bin/bash

# Navigate to the backend directory
cd back

# Start all services defined in the Docker Compose file
echo "Starting Django backend services..."
docker compose --env-file .env.dev -f docker-compose.dev.yml up -d

# Function to wait for the database to become available
wait_for_db() {
    echo "Waiting for database to become ready..."
    while ! nc -z db 5432; do
      sleep 1 # wait for 1 second before check again
    done
    echo "Database is ready!"
}

# Wait for the database to be ready
wait_for_db

# Apply Django migrations
echo "Applying Django migrations..."
docker-compose -f docker-compose.dev.yml exec web python manage.py migrate

# Navigate to the React app directory
cd ../react_app

# Start React services
echo "Starting React frontend..."
docker-compose up -d

echo "All services have been started successfully."
