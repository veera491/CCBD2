# micro_service_2/Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt gunicorn

EXPOSE 8000

ENV DATABASE_URL="postgresql://postgres:veera491@postgres-service:5432/ccbd_db"

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "micro_service_2_app:app"]
