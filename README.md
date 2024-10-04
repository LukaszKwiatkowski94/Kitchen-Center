# Kitchen Center

Kitchen Center is a Django-based web application that allows users to browse, add, and manage their favorite recipes. This application is containerized with Docker, making it easy to set up and run.

## Prerequisites

To run this project, you need the following installed on your machine:

- **Docker**: Ensure you have Docker installed. 
- **Docker Compose**: Docker Compose is usually included with Docker Desktop, but if you need to install it separately.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/LukaszKwiatkowski94/Kitchen-Center.git
cd kitchen-center
```

2. Build the Docker images:
```bash
docker-compose build
```

## Running the Application
1. Start the application with Docker Compose:
```bash
docker-compose up
```

2. Once the containers are up and running, the Kitchen Center app will be accessible at:

```
http://localhost:8000
```