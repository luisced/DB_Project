#!/bin/bash

# Define your network name
network_name="app_network"

# Function to wait for the database to become available
wait_for_db() {
    echo "Waiting for database to become ready..."
    while ! nc -z db 5432; do   
      sleep 1 # wait for 1 second before check again
    done
    echo "Database is ready!"
}


# Check if the network exists
network_exists=$(docker network ls | grep $network_name | awk '{print $2}')

# If the network doesn't exist, create it
if [ -z "$network_exists" ]; then
  echo "Creating network: $network_name"
  docker network create $network_name
else
  echo "Network $network_name already exists"
fi

# Navigate to the Django app directory and start the services
echo "Starting Django app..."
cd /back
docker compose --env-file .env.dev -f docker-compose.dev.yml up -d
echo "Waiting for database to become ready..."
wait_for_db
# Navigate to the React app directory and start the services
echo "Starting React app..."
cd react_app
docker-compose up -d

echo "All services are starting up..."
