# Base image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Run the app using uvicorn
CMD ["uvicorn", "app.main:asgi_app", "--host", "0.0.0.0", "--port", "5000"]
