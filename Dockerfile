# Use the official Python base image with the desired version (e.g., 3.10)
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application into the container
COPY . .

# Expose the port that the application will run on
EXPOSE 8000

# Define environment variables (if any) to be used in the container
ENV PYTHONUNBUFFERED=1

# Set the entry point for the container to run the FastAPI application with Uvicorn
ENTRYPOINT ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
