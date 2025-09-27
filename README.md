# Simple Users API with FastAPI & SQLite

FastAPi CRUD project is a RESTful API for managing users, built using FastAPI, SQLAlchemy, and SQLite. It demonstrates clean architecture, dependency injection, and best practices for Python web APIs.

## Features

- List all users
- Add new users
- Update existing users
- Delete users
- Uses SQLite for persistent storage
- Pydantic models for data validation
- SQLAlchemy for ORM and database operations

---

## Project Structure

```
├── app/
│   ├── main.py          # FastAPI app entrypoint
│   ├── database.py      # DB engine & session setup
│   ├── models.py        # SQLAlchemy & Pydantic models
│   └── routes/
│       └── users.py     # User CRUD endpoints
├── users.db             # SQLite database file
├── requirements.txt     # Python dependencies
├── api_venv/            # Virtual environment
└── README.md            # Project documentation
```

---

## Step-by-Step Setup & Usage

### 1. Clone the Repository

```powershell
git clone <your-repo-url>
cd "Public Api"
```

### 2. Create & Activate Virtual Environment

```powershell
python -m venv api_venv
api_venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Run the API Server

```powershell
uvicorn app.main:app --reload
```

The server will start at `http://127.0.0.1:8000/`

---

## API Endpoints & Usage

### 1. List All Users

**Request:**
```bash
curl -X GET "http://127.0.0.1:8000/users/" -H "accept: application/json"
```
**Response:**
```json
[
   {"id": 1, "name": "gg", "email": "gg@example.com"},
   {"id": 2, "name": "kk", "email": "kk@example.com"}
]
```

### 2. Add a New User

**Request:**
```bash
curl -X POST "http://127.0.0.1:8000/users/" \
       -H "accept: application/json" \
       -H "Content-Type: application/json" \
       -d '{"id": 3, "name": "Charlie", "email": "charlie@example.com"}'
```
**Response:**
```json
{
   "message": "User added successfully",
   "user": {"id": 3, "name": "cc", "email": "cc@example.com"}
}
```

### 3. Update a User

**Request:**
```bash
curl -X PUT "http://127.0.0.1:8000/users/3" \
       -H "accept: application/json" \
       -H "Content-Type: application/json" \
       -d '{"id": 3, "name": "ccb", "email": "ccb@example.com"}'
```
**Response:**
```json
{
   "message": "User updated successfully",
   "user": {"id": 3, "name": "ccb", "email": "ccb@example.com"}
}
```

### 4. Delete a User

**Request:**
```bash
curl -X DELETE "http://127.0.0.1:8000/users/3" -H "accept: application/json"
```
**Response:**
```json
{
   "message": "User deleted successfully"
}
```

---

## How It Works

- **FastAPI** provides automatic OpenAPI docs at `/docs` and `/redoc`.
- **SQLAlchemy** manages the SQLite database and user table.
- **Pydantic** validates request and response data.
- **Dependency Injection** is used for database sessions.

---

## Troubleshooting

- If you get a 500 Internal Server Error, check that `users.db` exists and is writable.
- Ensure all dependencies are installed and the virtual environment is activated.
- For database schema changes, delete `users.db` and restart the server to recreate tables.

---
