# Frontend API Guidelines

**Base URL:** `http://localhost:8000/api/v1`
*(Note: Route paths below append to Base URL)*

---

## Auth 

### 1. Register
- **POST** `/auth/register`
- **Body:**
  ```json
  {
    "email": "user@example.com",
    "password": "Secure123" 
  }
  ```
- **Response:** `{ "id": 1, "email": "user@example.com", "role": "user" }`

### 2. Login
- **POST** `/auth/login`
- **Body:**
  ```json
  {
    "email": "user@example.com",
    "password": "Secure123"
  }
  ```
- **Response:** `{ "access_token": "eyJhb...", "token_type": "bearer" }`

### 3. Get User Profile
- **GET** `/auth/me`
- **Headers:** `Authorization: Bearer <token>`
- **Response:** `{ "id": 1, "email": "user@example.com", "role": "user" }`

---

## Admin Auth (Admin Token Required)

### 1. List Users
- **GET** `/auth/admin/users`
- **Response:** `[ { "id": 1, "email": "user@ex.com", "role": "user" } ]`

### 2. Delete User
- **DELETE** `/auth/admin/users/{user_id}`
- **Response:** `{ "message": "User deleted successfully" }`

---

## Tasks (Token Required for All)

### 1. Create Task
- **POST** `/tasks/`
- **Body:** *(description is optional)*
  ```json
  {
    "title": "Build UI",
    "description": "Connect to API"
  }
  ```
- **Response:** `{ "id": 1, "title": "Build UI", "description": "Connect to API", "completed": false }`

### 2. List Tasks
- **GET** `/tasks/`
- **Response:** `[ { "id": 1, "title": "Task", "description": null, "completed": false } ]`
  *(Admins receive all system tasks; regular users receive only their own)*

### 3. Get Single Task
- **GET** `/tasks/{task_id}`
- **Response:** `{ "id": 1, "title": "Task", "description": "Details", "completed": false }`

### 4. Update Task
- **PUT** `/tasks/{task_id}`
- **Body:** *(All fields are optional, only send what needs updating)*
  ```json
  {
    "title": "New Title",
    "description": "New description",
    "completed": true
  }
  ```
- **Response:** Updated Task object.

### 5. Delete Task
- **DELETE** `/tasks/{task_id}`
- **Response:** `{ "message": "Task deleted" }`
