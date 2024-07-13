# Job Search Agent

## Overview

This project is a job search agent system that leverages AI agents to automate job search, application, and performance analysis processes. The backend is built using Flask and integrates with OpenAI's GPT models and Airtable as the database. The frontend is built with React to provide a user interface for interacting with the job search agents. The entire system is containerized using Docker.

## Project Structure

job-search-agent/
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── app.py
│   ├── agents.py
│   └── airtable_integration.py
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   ├── public/
│   └── src/
│       ├── App.js
│       ├── index.js
│       └── components/
│           └── JobSearchForm.js
└── docker-compose.yml

## Backend

### Dockerfile

Defines the Docker image for the backend, which installs Python dependencies and runs the Flask app.

### requirements.txt

Lists the Python dependencies required for the backend.

### app.py

Main Flask application file that defines API endpoints for job search, application, status update, performance analysis, and report generation.

### agents.py

Contains the logic for different job search agents, including job search, resume personalization, application tracking, and performance analysis.

### airtable_integration.py

Handles integration with Airtable, allowing the system to store and retrieve job application data.

## Frontend

### Dockerfile

Defines the Docker image for the frontend, which installs Node.js dependencies and runs the React app.

### package.json

Lists the JavaScript dependencies required for the frontend.

### App.js

Main React component that renders the job search form.

### index.js

Entry point for the React application.

### JobSearchForm.js

React component that handles the job search form and displays search results.

## Docker Compose

### docker-compose.yml

Defines the multi-container setup for the backend and frontend services.

## How to Run

### Prerequisites

- Docker and Docker Compose installed on your machine
- An Airtable account with an API key and base ID

### Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/job-search-agent.git
    cd job-search-agent
    ```

2. Create a `.env` file in the `backend` directory with the following environment variables:
    ```
    AIRTABLE_API_KEY=your_airtable_api_key
    AIRTABLE_BASE_ID=your_airtable_base_id
    ```

3. Build and run the Docker containers:
    ```bash
    docker-compose up --build
    ```

4. The backend will be accessible at `http://localhost:5000` and the frontend at `http://localhost:3000`.

### Usage

1. Open your browser and navigate to `http://localhost:3000`.

2. Enter job search criteria in the form and submit.

3. The backend will process the request using the job search agent and return relevant job postings.

4. Use the other endpoints for applying to jobs, updating application statuses, analyzing performance, and generating reports as needed.

### API Endpoints

- **POST /search_jobs**: Searches for jobs based on provided criteria.
- **POST /apply_to_job**: Applies to a job with a personalized resume and cover letter.
- **POST /update_application_status**: Updates the status of all job applications.
- **POST /analyze_performance**: Analyzes interview performance based on feedback.
- **GET /generate_report**: Generates a report of all job applications and performance insights.
