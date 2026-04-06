# Finance Dashboard Backend

## Overview

This is a backend system built using FastAPI for managing financial records with role-based access control. It allows different types of users to interact with financial data based on their permissions and provides summary insights for a dashboard.

---

## Features

* User management with roles (Admin, Analyst, Viewer)
* Financial records CRUD operations
* Dashboard summary APIs
* Role-based access restriction
* Input validation and error handling

---

## Tech Stack & Libraries Used

* **FastAPI**
  Modern, high-performance web framework for building APIs with Python.

* **Uvicorn**
  ASGI server used to run the FastAPI application.

* **SQLAlchemy**
  ORM used to interact with the database using Python objects instead of raw SQL.

* **SQLite**
  Lightweight database used for storing users and financial records.

---

## Project Setup

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd zor
```

---

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy
```

---

### 4. Run the application

```bash
uvicorn app.main:app --reload
```

---

### 5. Open in browser

* API Docs (Swagger UI):
  http://127.0.0.1:8000/docs

* Base URL:
  http://127.0.0.1:8000/

---

## API Endpoints

* `/user` → Manage users
* `/records` → Manage financial records
* `/dashboard` → View summary data

---

## Roles & Access Control

* **Admin**

  * Full access (Create, Update, Delete, View)

* **Analyst**

  * Can view records and dashboard insights

* **Viewer**

  * Can only view dashboard data

---

## Assumptions

* Authentication is simplified using role input in requests
* SQLite is used for simplicity and local development
* No external authentication system is implemented

---

## Sample API Requests & Responses

### 1. Create User

**Request:**

```json
POST /user
{
  "name": "Rony",
  "role": "admin",
  "is_active": true
}
```

**Response:**

```json
{
  "id": 1,
  "name": "Rony",
  "role": "admin",
  "is_active": true
}
```

---

### 2. Create Record (Admin only)

**Request:**

```json
POST /records?role=admin
{
  "amount": 5000,
  "type": "income",
  "category": "salary",
  "date": "2026-04-06",
  "notes": "Monthly salary"
}
```

**Response:**

```json
{
  "message": "Record created successfully"
}
```

**Error (if not admin):**

```json
{
  "detail": "Admin access required"
}
```

---

### 3. Get Records

**Request:**

```json
GET /records
```

**Response:**

```json
[
  {
    "id": 1,
    "amount": 5000,
    "type": "income",
    "category": "salary"
  }
]
```

---

### 4. Dashboard Summary

**Request:**

```json
GET /dashboard
```

**Response:**

```json
{
  "total_income": 5000,
  "total_expense": 3000,
  "balance": 2000
}
```

---

## Future Improvements

* JWT Authentication
* Pagination & filtering
* Advanced analytics (monthly trends, category insights)
* Deployment (Render / Railway / AWS)

---

## Author

Backend Developer Intern Assignment Submission
