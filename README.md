# Student Info
Sviderskyi Yaroslav Petrovych

# Objective
Create a simple containerized Flask API with two endpoints.

# Running Locally
1. (Optional) Set up and activate a virtual environment: `python3 -m venv venv && source ./venv/bin/activate`
2. Install the dependencies: `pip install -r requirements.txt`
3. Start the application: `flask run -p 3030`

# Running in a Container
1. Ensure Docker is installed on your system.
2. Start Docker.
3. Build the Docker image: `docker build -t flask_api_example .`
4. Run the container: `docker run -it --rm --network=host -e PORT=8080 flask_api_example`

Note: Replace `flask_api_example` with any name you prefer.

# Running with Docker-Compose
1. Install Docker-Compose.
2. Build the container: `docker-compose build`
3. Start the application: `docker-compose up`

# Usage
Send a GET request to the `/healthcheck` endpoint. The application responds with a JSON object containing the current time in Kyiv, the server status, and a status code of 200. The response has the following format:  
```json
{ 
  "date": "string", 
  "status": "string" 
}
