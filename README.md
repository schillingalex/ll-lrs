An adaptive curriculum and learner-state service for a language-learning game, built with Python and FastAPI.

# Usage

## Docker

The container can be built via:

```bash
docker build -t ll-lrs .
```

The container exposes port 8000, so bind to it when running:

```bash
docker run -p 8000:8000 ll-lrs
```

You can check if the container is running by navigating to `localhost:8000/health`,
which should return `{"status": "ok"}`.

## Docker Compose

Docker Compose is used to start the entire stack, i.e., the API and all the backend
services required to run it, such as PostgreSQL.

Validate the configuration via:

```bash
docker compose config
```

Bring up the entire stack:

```bash
docker compose up -d
```

Check that the API and PostgreSQL services are running (should list two containers,
the PostgreSQL container should report "healthy" under status):

```bash
docker compose ps
```

Inspect the logs of individual services through `docker compose logs <service>`, e.g.:

```bash
docker compose logs db
```

Check that the database is up and running (should return 1 row and 1 column with "1"):

```bash
docker compose exec db sh -c 'psql -d "$POSTGRES_DB" -U "$POSTGRES_USER" -w -c "SELECT 1"'
```

To stop the services:

```bash
docker compose down
```

To remove the volume and start over with a clean database:

```bash
docker compose down --volumes
```

## Local (dev)

```bash
uv run fastapi dev src/ll_lrs/main.py
```

# Testing

```bash
uv run pytest
```
