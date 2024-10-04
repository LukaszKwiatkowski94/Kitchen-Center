# Select Python Base Image
FROM python:3.11-slim

# Set an environment variable that disables Python output buffering
ENV PYTHONUNBUFFERED 1

# Create a directory in the application container
WORKDIR /app

# Install dependencies (Django)
RUN pip install --upgrade pip && pip install Django==5.1.1 
RUN pip install python-dotenv

# Copy the entire project to the /app directory in the container
COPY . /app/

# Opening of port 8000 in container
EXPOSE 8000

# Start Django development server on port 0.0.0.0:8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
