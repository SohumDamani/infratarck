# InfraTrack

InfraTrack is a cloud infrastructure tracking backend (FastAPI) with a planned frontend and infrastructure-as-code. The current implementation includes an API for managing infrastructure assets and a PostgreSQL database via Docker.

## 📂 Project Structure

InfraTrack/
├── backend/ # FastAPI backend (containerized)
│ ├── app/
│ │ ├── api/
│ │ │ ├── assets.py # Assets endpoints (POST/GET)
│ │ │ ├── health.py # Health check
│ │ │ └── schemas.py # Pydantic schemas
│ │ ├── db/
│ │ │ ├── session.py # SQLAlchemy engine/session and Base
│ │ │ ├── models.py # ORM models (e.g., Asset)
│ │ │ └── create_tables.py# Script to create tables
│ │ ├── main.py # FastAPI app entrypoint
│ │ └── requirements.txt # Python dependencies
│ └── Dockerfile # Backend image
├── docker-compose.yml # Orchestration (API + Postgres)
├── frontend/ # Placeholder for React app (future)
├── infra/ # Placeholder for Terraform/IaC (future)
├── docs/ # Documentation (future)
└── README.md

Note: `frontend/`, `infra/`, and `docs/` are placeholders for future expansion.

## 🚀 Getting Started

### Prerequisites

- Docker and Docker Compose
- Alternatively for local (non-Docker) runs: Python 3.12+, PostgreSQL

### Quick start (Docker Compose)

From the repo root:

```bash
docker compose up --build
```

This will:

- Build and start the backend at `http://localhost:8000`
- Start PostgreSQL at `localhost:5432`
- Set `DATABASE_URL` for the backend automatically (see `docker-compose.yml`)

Visit:

- API root: `http://localhost:8000/`
- Health: `http://localhost:8000/api/health`
- Interactive docs (Swagger): `http://localhost:8000/docs`

### Local development without Docker

1. Create and export `DATABASE_URL` to point to your Postgres instance:

```bash
export DATABASE_URL="postgresql://infratrack_user:infratrack_pass@localhost:5432/infratrack_db"
```

2. Install dependencies and run the API:

```bash
cd backend/app
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

3. Create tables (first run only):

```bash
python -c "from db.create_tables import Base, engine; Base.metadata.create_all(bind=engine)"
# Or (when running from backend/app): python db/create_tables.py
```

4. Start the server:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 📘 API Overview

Base URL when running locally: `http://localhost:8000`

- GET `/` — API root message
- GET `/api/health` — Health check
- GET `/assets/` — List all assets
- POST `/assets/` — Create an asset

### Create Asset (POST `/assets/`)

Request body:

```json
{
  "name": "Server-01",
  "category": "server",
  "price": 1200.5,
  "quantity": 10
}
```

Notes:

- Each `(name, category)` pair must be unique.
- Validation: `price >= 0`, `quantity >= 0`.

Example curl:

```bash
curl -X POST http://localhost:8000/assets/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Server-01","category":"server","price":1200.5,"quantity":10}'
```

## 🗄️ Database

- SQLAlchemy is configured in `backend/app/db/session.py` using `DATABASE_URL`.
- ORM models live in `backend/app/db/models.py` (e.g., `Asset`).
- Tables can be created via `backend/app/db/create_tables.py` or the one-liner shown above.

## 🧪 Dev Tooling

- Lint/format: `flake8`, `black`, `isort` are included in `requirements.txt`.
  - Example (from `backend/app`):
    - `flake8`
    - `black .`
    - `isort .`

## 🔐 Environment Variables

- `DATABASE_URL`: PostgreSQL connection string.
  - Docker Compose sets: `postgresql://infratrack_user:infratrack_pass@db:5432/infratrack_db`
  - Local example: `postgresql://infratrack_user:infratrack_pass@localhost:5432/infratrack_db`

## 🧭 Roadmap

- Expand asset inventory features and filtering
- Add authentication and user management
- Implement React frontend and CI/CD
- Infrastructure as code under `infra/`
