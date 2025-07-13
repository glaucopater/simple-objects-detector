# Use an official Python runtime as a parent image
FROM python:3.13-slim


# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

# Copy the rest of the application's code to the container
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP web_app.py

# Run the command to start the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
