# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    gcc \
    libc-dev \
    libffi-dev \
    libssl-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Upgrade pip and install virtualenv
RUN python -m pip install --upgrade pip setuptools wheel virtualenv

# Create a virtual environment and install dependencies
RUN python -m virtualenv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
COPY . .

# Expose the port your FastAPI app runs on (default is 8000)
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


# sudo docker build -t fastapi-app .
# sudo docker run -p 8000:8000 fastapi-app
