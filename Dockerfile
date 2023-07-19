FROM python:3.9

RUN apt-get update && apt-get install -y python3-pip
RUN apt-get install libgeos-dev -y

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .


WORKDIR /app_crud

CMD ["python3", "-u", "/main.py"]
