FROM python:3.11.8-slim-bullseye
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3-pip -y
RUN pip3 install -U pip
RUN python3 -m pip install --upgrade pip

COPY . /app/
WORKDIR /app/
RUN pip3 install -U -r requirement.txt


EXPOSE 8000

RUN python3 manage.py migrate --run-syncdb
CMD ["python3","manage.py", "runserver", "0.0.0.0:8000"]