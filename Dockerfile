FROM python:3.11.8-slim-bullseye
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3-pip -y
RUN apt-get install sqlite3  -y
RUN pip3 install -U pip
RUN python3 -m pip install --upgrade pip

COPY . /app/
WORKDIR /app/
RUN pip3 install -U -r requirement.txt

EXPOSE 8000

RUN python3 manage.py migrate --run-syncdb
RUN python3 manage.py collectstatic
CMD ["gunicorn", "--bind", "0.0.0.0:8000", 'configs.wsgi']