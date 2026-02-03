# Address Book API

A minimal Address Book API built with FastAPI, SQLite, and SQLAlchemy.

## Features
- Create, Update, Delete addresses.
- Retrieve addresses within a given distance and location (Latitude/Longitude).
- Automatic database validation.
- SQLite database storage.
- Alembic migrations integrated.
- SQLAlchemy for ORM.

## Project Structure
- `api/models/address.py`: Database models.
- `api/schemas/schemas.py`: Pydantic schemas for validation.
- `api/routers/address.py`: API endpoints.
- `api/service/address_service.py`: Business logic and database interactions.
- `core/db`: Database configuration.
- `alembic/`: Database migration scripts.

## Requirements
- Python 3.8+
- Dependencies listed in `requirements.txt`

## Execution

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Database Migrations
Initialize the database using Alembic:
```bash
# Generate migration script
alembic revision --autogenerate -m "Initial_migration"

# Apply migration
alembic upgrade head
```

### 3. Run the Application
```bash
uvicorn main:app --reload
```
The application will be available at `http://127.0.0.1:8000`.

### 4. API Documentation
Open `http://127.0.0.1:8000/docs` to view the interactive Swagger UI.

## Testing
You can run the provided manual check script:
```bash
python3 api/tests/tests_address.py
```
