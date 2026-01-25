FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir fastapi[standard] sqlalchemy psycopg2-binary python-dotenv pwdlib[argon2]

COPY app ./app

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
