# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt gunicorn
#docker images
# Expose port 5000 for the Flask app
EXPOSE 5000
# Define environment variable for Flask
ENV DATABASE_URL="postgresql://postgres:veera491@postgres-service:5432/ccbd_db"

# Run the command to start the application with Gunicorn
#CMD ["gunicorn", "--bind", "0.0.0.0:5000", "micro_service_1_app:app"]
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--threads", "4", "micro_service_1_app:app"]