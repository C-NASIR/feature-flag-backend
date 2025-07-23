# Feature Flag Backend

A backend service for managing feature flags built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.

This system enables dynamic toggling of features via RESTful APIs, supporting scalable and maintainable feature management.

---

## Table of Contents

- [Overview](#overview)

- [Features](#features)

- [Tech Stack](#tech-stack)

- [Project Structure](#project-structure)

- [Setup & Installation](#setup--installation)

- [Environment Variables](#environment-variables)

- [Database & Migrations](#database--migrations)

- [Running the Application](#running-the-application)

- [API Endpoints](#api-endpoints)

- [Testing](#testing)

- [Contributing](#contributing)

- [License](#license)

---

## Overview

Feature flags allow developers to enable or disable features dynamically without deploying new code, facilitating controlled rollouts, A/B testing, and quick rollbacks.

This backend provides CRUD operations on feature flags with UUID identifiers, timestamp tracking, and extensible design for future features like multi-tenancy and environment-specific flags.

---

## Features

- Create, Read, Update, Delete (CRUD) feature flags

- UUID primary keys for global uniqueness

- Flags have keys, names, descriptions, enabled status

- Automatic `created_at` and `updated_at` timestamps

- Pydantic schemas for request validation and response models

- SQLAlchemy ORM integration with PostgreSQL

- Alembic for database schema migrations

- Environment variable based configuration via `.env`

- Modular folder structure separating models, schemas, routers, services, and db setup

---

## Tech Stack

- **FastAPI** — Python web framework for building APIs

- **Uvicorn** — ASGI server to run FastAPI apps

- **SQLAlchemy** — Object Relational Mapper (ORM) for DB interactions

- **PostgreSQL** — Relational database

- **Alembic** — Database migration tool

- **Pydantic** — Data validation and serialization

- **Python 3.13+**

---

## Project Structure

feature_flag_backend/

── src/

│ ── main.py # FastAPI app entrypoint

│ ── models/

│ │ └── flag.py # SQLAlchemy models

│ ── schemas/

│ │ ── flag.py # Pydantic schemas

│ ── routers/

│ │ ── flag.py # API routes for flags

│ ── services/

│ │ ── flag_service.py # Business logic and DB operations

│ ── db/

│ │ ── session.py # DB connection/session management

│ │ ── base.py # Base class for models

│ ── alembic/ # Alembic migration scripts (generated)

── .env # Environment variables (ignored by git)

── alembic.ini # Alembic configuration file

── requirements.txt # Python dependencies

── README.md # This file

---

## Setup & Installation

### Prerequisites

- Python 3.13+

- PostgreSQL installed and running

- `brew` (macOS) or appropriate package manager

### Steps

**Clone the repository**

```bash
git clone https://github.com/C-NASIR/feature-flag-backend.git
cd feature_flag_backend
```

**Create and activate a virtual environment**

```
python3 -m venv .venv
source .venv/bin/activate
```

**Install dependencies**

```
pip install -r requirements.txt
```

**Set up PostgreSQL database**

- tart PostgreSQL service (e.g., brew services start postgresql)

- Create a database with a descriptive name:

```
createdb feature_flag_db
```

**Configure environment variables**

Create a .env file in the root directory:

```
DATABASE_URL=postgresql+psycopg2://yourusername:yourpassword@localhost:5432/feature_flag_db
```

### Database & Migrations

**Initialize Alembic (if not done)**

```
alembic init src/alembic
```

**Create migration after model changes**

```
alembic revision --autogenerate -m "create flags table"
alembic upgrade head
```

### Running the Application

Run the FastAPI app with Uvicorn:

```
uvicorn src.main:app --reload
```

- Access Swagger UI docs: http://127.0.0.1:8000/docs
- Access Redoc docs: http://127.0.0.1:8000/redoc

## license

MIT License © C NASIR
