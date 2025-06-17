FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml .

RUN pip install --upgrade pip \
    && pip install uv \
    && uv sync

COPY app.py .

EXPOSE 5000

CMD ["uv", "run", "python", "app.py"]
