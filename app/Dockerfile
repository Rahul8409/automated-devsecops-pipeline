# Python Image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY app.py .

# Expose the port that the application will run on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]