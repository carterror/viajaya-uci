FROM python:3.11.8-slim

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y python3-pip sqlite3 && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip && \
    pip3 install -r requirement.txt

COPY . /app/
WORKDIR /app/

RUN python3 manage.py migrate --run-syncdb
RUN python3 manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "configs.wsgi:application"]
