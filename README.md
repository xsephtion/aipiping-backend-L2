# AI Piping Challenge

## Introduction

Backend, Python + FastAPI

Objective: Create a simple FastAPI application that serves an endpoint to recommend three things to do in a given country during a specific season by consulting the OpenAI API.

## Getting Started

To run the application locally, follow these steps:

1. Install the required dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the application using `uvicorn`:

   ```bash
   uvicorn main:app --reload --port 3000
   ```

   This will start the application on port 3000 with automatic reloading enabled.

## Running Tests

To run the tests for the application, you can use `pytest`. First, ensure that `pytest` is installed in your virtual environment:

```bash
pip install pytest
```

Then, execute the tests by running:

```bash
pytest tests/test_main.py
```

## Docker

### Building the Docker Image

To run the application within a Docker container, you need to build a Docker image first. Use the following command to build the image:

```bash
docker build -t recommendationimage .
```

### Starting the Docker Container

Once you have built the Docker image, you can start a Docker container with the following command:

```bash
docker run -d --name recocontainer -p 80:80 recommendationimage
```

This command will run a Docker container named "recocontainer" in detached mode, mapping port 80 on your host machine to port 80 in the container.

## Usage

After starting the application or the Docker container, you can access it by navigating to http://localhost:3000 (if running locally) or http://localhost (if running in a Docker container).
