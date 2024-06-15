FROM python:3.8

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0

RUN mkdir app

WORKDIR /app
COPY . /app

COPY requirements_tg.txt /app/requirements.txt
RUN pip install --default-timeout=1200 -r /app/requirements.txt


ENTRYPOINT ["python3", "telegram-bot/bot.py"]
