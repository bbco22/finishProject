FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

COPY . .

EXPOSE 8000

ENTRYPOINT ["python3", "manage.py"]
