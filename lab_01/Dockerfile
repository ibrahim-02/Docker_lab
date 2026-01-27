FROM python:3.10-slim

WORKDIR /app

# Copy requirements first (for caching)
COPY src/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ .

CMD ["python", "app.py"]
