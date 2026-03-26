# Backend API Assignment

RESTful API built with FastAPI and Prisma, featuring JWT authentication, role-based access control (RBAC), and Task CRUD functionality.

## Tech Stack
- **Framework:** FastAPI (Python)
- **Database:** PostgreSQL
- **ORM:** Prisma Client Python
- **Security:** JWT Authentication, bcrypt Hashing

## Core Features
- User registration and login APIs.
- Role-based scoping (user vs admin).
- Complete CRUD API for Tasks.
  - Users manage their own tasks.
  - Admins can access and manage all tasks globally.
- Admin route to view and delete registered users.
- Input validation via Pydantic.

## Local Setup

1. **Environment Config**
Create `.env`:
```env
DATABASE_URL="postgresql://username:password@localhost:5432/dbname"
SECRET_KEY="your_secret_key"
ALGORITHM="HS256"
```

2. **Dependencies & DB Instantiation**
```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows
pip install -r requirements.txt

prisma generate
prisma db push
```

3. **Run Server**
```bash
uvicorn app.main:app --reload
```

## API Endpoints

Interactive Swagger documentation is auto-generated at `http://localhost:8000/docs` upon launch.

**Auth & Users**
- `POST /api/v1/auth/register` (Public)
- `POST /api/v1/auth/login` (Public)
- `GET /api/v1/auth/me` (Protected)
- `GET /api/v1/auth/admin/users` (Admin)
- `DELETE /api/v1/auth/admin/users/{id}` (Admin)

**Tasks**
- `POST /api/v1/tasks/` (Protected - Create)
- `GET /api/v1/tasks/` (Protected - List [Admin sees all, User sees own])
- `GET /api/v1/tasks/{id}` (Protected - Fetch)
- `PUT /api/v1/tasks/{id}` (Protected - Update)
- `DELETE /api/v1/tasks/{id}` (Protected - Delete)

*(Note: New users default to the "user" role. Provision admins manually via database updates).*

## Scalability Note
Designed for immediate scalability:
- **Stateless & Microservice-Ready:** Auth and Task modules are completely decoupled. Services can be easily split into independent containers.
- **Asynchronous Architecture:** Python's `asyncio` is used universally, meaning database operations do not block the thread.
- **Caching & Sharding Potential:** The decoupled design supports seamless Redis layer insertion before Postgres reads, and the data schema is structured securely for horizontal sharding.
