A backend and API for a learning record store with Python and FastAPI

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

## Local (dev)

```bash
uv run fastapi dev src/ll_lrs/main.py
```

# Testing

```bash
uv run pytest
```
