# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV APP_ENV=production \
    APP_PORT=1000

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install FastAPI and Uvicorn
RUN pip install --no-cache-dir fastapi uvicorn

# Expose the port FastAPI will run on
EXPOSE 1000

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "1000"]