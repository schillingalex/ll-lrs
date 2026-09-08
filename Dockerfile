FROM python:3.13-slim

WORKDIR /lrs

EXPOSE 8000

# uv installation
COPY --from=ghcr.io/astral-sh/uv:0.12.10 /uv /uvx /bin/
ENV UV_NO_DEV=1

COPY uv.lock pyproject.toml README.md /lrs/
RUN uv sync --locked --no-install-project

ENV PATH="$PATH:/lrs/.venv/bin"

COPY ./src /lrs/src
RUN uv sync --locked

CMD ["fastapi", "run", "src/ll_lrs/main.py", "--host", "0.0.0.0", "--port", "8000"]
