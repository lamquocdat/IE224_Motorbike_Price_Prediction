# webapp/Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Copy only the requirements file, to leverage Docker cache
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Load environment variables from .env file
RUN pip install python-dotenv

# Set the environment variable
ENV FLASK_APP app.py

# Set the default port to 5000
EXPOSE 5000

# Expose the port that Flask will run on
EXPOSE $PORT

# Command to run the application
CMD ["sh", "-c", "flask run --host=0.0.0.0 --port=$PORT"]
