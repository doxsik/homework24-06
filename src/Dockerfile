FROM python:3.10-slim

WORKDIR /bookstore/src

COPY . .

ENV PYTHONBUFFERED=1
ENV PYTHONDOTWRITEBYTECODE=1

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    vim \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && gunicorn reverence.wsgi:application --bind 0.0.0.0:8000"]



