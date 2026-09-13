FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY data ./data
COPY models ./models
COPY results ./results
COPY run.py .

CMD ["python", "-m", "app.train"]