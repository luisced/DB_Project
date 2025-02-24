# Django REST Framework Template Project

A production-ready Django REST Framework template with JWT authentication, PostgreSQL, and Docker support.

## Environment Variables

The project uses the following environment variables (defined in `.env.dev` for development):

### Database Configuration
```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
POSTGRES_PORT=5432
DB_ENGINE=django.db.backends.postgresql
POSTGRES_HOST=db
```

### Django Settings
```
DEBUG=True
DJANGO_SETTINGS_MODULE=server.settings
SECRET_KEY='your-secret-key'
```

### Default Superuser
```
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=admin
```

## Quick Start

1. Copy `.env.dev` to create your environment file:
```bash
cp .env.dev .env
```

2. Start the development server:
```bash
docker-compose -f docker-compose.dev.yml up --build
```

3. Run migrations inside the container:
```bash
# Run migrations
docker exec back-app python manage.py migrate

# Create superuser (if needed)
docker exec back-app python manage.py createsuperuser

# Make migrations (when you modify models)
docker exec back-app python manage.py makemigrations
```

4. Access the API at http://localhost:8000

## Core Endpoints

### Health Check
```bash
# Check API health
curl http://localhost:8000/api/health/
```

### Authentication
```bash
# Login - Get JWT tokens
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin"}'

# Refresh token
curl -X POST http://localhost:8000/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "your-refresh-token"}'

# Verify token
curl -X POST http://localhost:8000/api/token/verify/ \
  -H "Content-Type: application/json" \
  -d '{"token": "your-access-token"}'
```

### Users
```bash
# List users (requires authentication)
curl http://localhost:8000/api/users/ \
  -H "Authorization: Bearer your-access-token"

# Create user
curl -X POST http://localhost:8000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{"username": "newuser", "password": "userpass", "email": "user@example.com"}'
```

### Example Endpoints
```bash
# List examples (requires authentication)
curl http://localhost:8000/api/examples/ \
  -H "Authorization: Bearer your-access-token"

# Create example
curl -X POST http://localhost:8000/api/examples/ \
  -H "Authorization: Bearer your-access-token" \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Example", "description": "Test description", "quantity": 1}'

# Get example stats
curl http://localhost:8000/api/examples/stats/ \
  -H "Authorization: Bearer your-access-token"

# Toggle example active status
curl -X POST http://localhost:8000/api/examples/1/toggle_active/ \
  -H "Authorization: Bearer your-access-token"
```

## Project Structure

```
back/
├── app/
│   ├── models/          # Database models
│   ├── serializers/     # API serializers
│   ├── urls/           # URL routing
│   ├── views/          # API views
│   └── utils/          # Utility functions
└── server/             # Project settings
```

## Example Implementation

The project includes example implementations showing best practices for:
- Models (`app/models/example_model.py`)
- Serializers (`app/serializers/example_serializers.py`)
- ViewSets (`app/views/example_views.py`)
- URL routing (`app/urls/example_urls.py`)

Use these as templates when adding new features to your project.
