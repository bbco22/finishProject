FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

COPY . .

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
