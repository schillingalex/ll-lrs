# Alembic

## Auto-generate Revision

Based on having a .env file (template in .env.example) and .env.host, which should contain the
configurations to get from the host machine into the db container, e.g.:

```ini
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=8001
```

Through `uv run`'s `--env-file` arg, we can first add the base .env and then the .env.host
file to override the required values for host-to-container connection.

```bash
uv run --env-file .env --env-file .env.host alembic revision --autogenerate -m retrieval_attempt
```

## Migrate to the latest revision

```bash
uv run --env-file .env --env-file .env.host alembic upgrade head
```
