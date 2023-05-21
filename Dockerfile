FROM python:3.9-alpine

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app


RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000

