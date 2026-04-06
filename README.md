# Finance Dashboard Backend

## Overview

This is a backend system built using FastAPI for managing financial records with role-based access control.

## Features

* User management with roles (Admin, Analyst, Viewer)
* Financial records CRUD operations
* Dashboard summary APIs
* Role-based access restriction
* Input validation and error handling

## Tech Stack

* FastAPI
* SQLite
* SQLAlchemy

## How to Run

```bash
pip install fastapi uvicorn sqlalchemy
uvicorn app.main:app --reload
```

## API Endpoints

* `/user` → Manage users
* `/records` → Manage financial records
* `/dashboard` → View summary

## Roles

* Admin → Full access
* Analyst → Read + insights
* Viewer → Read only

## Assumptions

* Authentication is simplified using role input
* SQLite used for simplicity

## Author

Backend Developer Intern Assignment Submission
