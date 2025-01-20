FROM python:3.12.3

WORKDIR /bookstore/src

COPY . .

ENV PYTHONBUFFERED=1
ENV PYTHONDOTWRITEBYTECODE=1

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]



