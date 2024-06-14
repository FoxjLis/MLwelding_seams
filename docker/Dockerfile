FROM python:3.8

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0

WORKDIR /app
COPY ../../../../PycharmProjects/haha_docker /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

RUN mkdir -p /uploads && chmod -R 777 /uploads
RUN mkdir -p /app && chmod -R 777 /app
RUN mkdir -p /results && chmod -R 777 /app/results

ENV FLASK_APP=__init__.py

CMD ["flask", "run", "--host=0.0.0.0"]