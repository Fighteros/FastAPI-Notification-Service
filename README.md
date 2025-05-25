# FastAPI Notification Service

A FastAPI-based notification service that manages user reminders and sends notifications. The service tracks users with upcoming reminders and provides endpoints to manage and query user data.

## Features

- User management with reminder dates
- Automatic detection of users with reminders due in the next hour
- RESTful API endpoints for user operations
- SQLAlchemy for database operations
- Timezone-aware datetime handling

## Project Structure

```
.
├── app.py                 # Main FastAPI application
├── db/
│   ├── __init__.py
│   └── database.py       # Database configuration
├── users/
│   ├── __init__.py
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic models
│   ├── routes.py         # API endpoints
│   ├── service.py        # Business logic
│   └── seeders.py        # Database seeding
└── requirements.txt      # Project dependencies
```

## Setup

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the database seeder:

```bash
python seed_db.py
```

4. Start the application:

```bash
uvicorn app:app --reload
```

## API Endpoints

### Users

#### GET /users/

Retrieve all users with optional pagination.

- Query Parameters:
  - `skip`: Number of records to skip (default: 0)
  - `limit`: Maximum number of records to return (default: 100)

#### GET /users/due-reminders

Retrieve users who have reminders due in the next hour.

- Returns only active users
- Orders results by reminder date (ascending)
- Excludes users with past reminders or reminders beyond one hour

## Database Models

### User

- `id`: Integer (Primary Key)
- `email`: String (Unique)
- `full_name`: String
- `reminder_date`: DateTime (Timezone-aware)
- `is_active`: Boolean
- `created_at`: DateTime
- `updated_at`: DateTime

## Development

### Seeding Test Data

The seeder creates test users with various reminder scenarios:

- Users with reminders due within the next hour
- Users with reminders due beyond the next hour
- Inactive users
- Users with past reminders

Run the seeder:

```bash
python seed_db.py
```

### Timezone Handling

The application uses timezone-aware datetime objects (UTC) for all date/time operations to ensure consistent behavior across different timezones.

## Requirements

- Python 3.8+
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn

## License

MIT
