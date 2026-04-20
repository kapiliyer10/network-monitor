FROM python:3.10-slim

ENV PYTHONPATH=/app

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y iputils-ping

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p logs

CMD ["python", "src/main.py"]
