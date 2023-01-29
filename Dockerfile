FROM python:3.10

WORKDIR /app


COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY config /app/extern/config
COPY logs /app/extern/logs
COPY nflbot /app/nflbot
COPY bot.py /app/bot.py

CMD ["python", "bot.py"]

