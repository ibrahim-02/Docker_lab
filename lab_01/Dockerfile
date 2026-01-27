# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file first (for caching)
COPY lab_01/src/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY lab_01/src/ .

# Run the script
CMD ["python", "main.py"]
