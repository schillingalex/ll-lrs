# Alembic

## Auto-generate Revision

> Autogeneration only works if the database container is running.

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

## Downgrade to Revision

Target revision is `base` in this case, i.e., before everything.

```bash
uv run --env-file .env --env-file .env.host alembic downgrade base
```

## Checking the Status of a Table

```bash
docker compose exec db sh -c 'psql -d "$POSTGRES_DB" -U "$POSTGRES_USER" -w -c "SELECT * FROM retrieval_attempts"'
```
