FROM python:3.10-slim

WORKDIR /app

ENV TOKEN=6313487970:AAFTTlck6BdTRqUkx1OMPXYBVYJ6ayFWZuc

COPY bot.py .
COPY cfg.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "bot.py"]

