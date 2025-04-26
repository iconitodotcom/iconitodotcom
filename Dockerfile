# Use an official Python base image
FROM python:3.11-slim

LABEL MAINTAINER="Julio Conchas <conchasjimenez@gmail.com>"

# Set working directory inside the container
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy pyproject.toml and poetry.lock first
COPY pyproject.toml poetry.lock* /app/

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copy application files
COPY . .

#Expose Flask port
#EXPOSE 5000
#Fly port
EXPOSE 8080

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

#Run the Flask app
#CMD ["flask", "run", "--host=0.0.0.0:8080"]
CMD ["flask", "run"]
