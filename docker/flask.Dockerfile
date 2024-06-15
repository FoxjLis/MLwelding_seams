FROM python:3.8

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0


ADD requirements_flask.txt requirements.txt
RUN pip install --default-timeout=1200 -r requirements.txt


RUN mkdir app
WORKDIR /app
ADD ./ /app/

ENV FLASK_APP=__init__.py

CMD ["python", "__init__.py"]
