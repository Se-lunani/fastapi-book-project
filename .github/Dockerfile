# Use an official lightweight Python image.
FROM python:3.9-slim

# Set environment variables.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory.
WORKDIR /app

# Install system dependencies (if needed) and pip.
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Copy and install Python dependencies.
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire application code.
COPY . .

# Expose the port on which FastAPI will run.
EXPOSE 8000

# Start the FastAPI application using Uvicorn.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

