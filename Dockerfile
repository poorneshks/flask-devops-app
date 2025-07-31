# Use an official Python runtime as base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirement file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Expose the port gunicorn will run on
EXPOSE 8000

# Start the app using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
