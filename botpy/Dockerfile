FROM python:3.10-slim

WORKDIR /app

ENV TOKEN='insert your token here'

COPY bot.py .
COPY cfg.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "bot.py"]

