# Use the official Python image as the base image
FROM python:3.9

# Set the working directory
WORKDIR /code

# Define the environment variable OPEN_AI_KEY
ENV OPEN_AI_KEY=INSERTYOURKEYHERE

# Copy the requirements file and install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Define the command to run the application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
