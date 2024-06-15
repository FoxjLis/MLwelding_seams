FROM python:3.8

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0

RUN mkdir app

WORKDIR /app
COPY . /app

COPY requirements_tg.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

ENTRYPOINT ["python3", "bot.py"]