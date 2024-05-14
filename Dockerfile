FROM python:3.10-alpine

WORKDIR /app

RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY config /app/extern/config
COPY logs /app/extern/logs
COPY nflbot /app/nflbot
COPY bot.py /app/bot.py

CMD ["python", "bot.py"]
