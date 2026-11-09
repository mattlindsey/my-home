# my-home
Home dashboard

FastAPI backend (SQLite via SQLModel/Pydantic) + React (Vite) frontend.

## Backend

```bash
uv sync
uv run alembic upgrade head   # create/update my_home.db (run after pulling new migrations)
uv run my-home                # serves http://127.0.0.1:8000
uv run pytest
```

### Database migrations (Alembic)

The schema lives in `migrations/versions/`; the server never creates or alters tables.
After changing a model in `src/my_home/db.py`:

```bash
uv run alembic revision --autogenerate -m "describe the change"
# review the generated file, then:
uv run alembic upgrade head
```

Set `MY_HOME_DATABASE_URL` to use a different database (default `sqlite:///my_home.db`).

Endpoint: `GET /api/hi` → `{"message": "Hi Matt!"}` (name read from the `person` table).

## Frontend

Requires Node.js 18+.

```bash
cd frontend
npm install
npm run dev             # http://localhost:5173, proxies /api to the backend
```
