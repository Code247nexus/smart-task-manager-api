# Smart Task Manager API

A production-style Task Management REST API built using Django REST Framework with JWT Authentication and MySQL.

---

## Features

- User Registration
- JWT Login & Refresh Token
- Custom User Model
- Role-Based User System
- Project CRUD
- Task CRUD
- Task Filtering
- AI Priority Suggestion
- Swagger API Documentation
- MySQL Database
- Protected APIs

---

## Tech Stack

- Python
- Django
- Django REST Framework
- MySQL
- JWT
- Swagger
- Thunder Client

---

## API Endpoints

### Authentication

POST /api/auth/register/

POST /api/auth/login/

POST /api/auth/refresh/

GET /api/auth/profile/

---

### Projects

GET /api/projects/

POST /api/projects/

PUT /api/projects/{id}/

DELETE /api/projects/{id}/

---

### Tasks

GET /api/tasks/

POST /api/tasks/

PATCH /api/tasks/{id}/

DELETE /api/tasks/{id}/

GET /api/tasks/?status=TODO

GET /api/tasks/?priority=HIGH

POST /api/tasks/suggest_priority/

---

## Swagger

```
/swagger/
```

---

## Author

Aditya Jha