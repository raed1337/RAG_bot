Here's the merged `README.md` file for your Multi-Agent Human Resource Manager Chatbot project with the FastAPI secure application details:

# Multi-Agent Human Resource Manager Chatbot

## Overview

This project is a multi-agent chatbot designed to assist human resource managers with various tasks. The chatbot is built using the LangChain framework and leverages multiple agents to handle different parts of the conversation flow, including greeting the user, identifying the user's request, investigating problems, summarizing the conversation, and providing recommendations. The project also includes a secure FastAPI application for handling employee information from a CSV file.

## Project Structure

```
chatbot_project/
├── agents/
│   ├── __init__.py
│   ├── agent.py
│   ├── greeting_agent.py
│   ├── identification_agent.py
│   ├── investigation_agent.py
│   ├── summarization_agent.py
│   ├── recommendation_agent.py
│   ├── validation_agent.py
├── state_tracker/
│   ├── __init__.py
│   ├── state_tracker.py
├── main.py
├── server.py
├── requirements.txt
├── Dockerfile
├── .env
├── routers/
│   └── query_router.py
├── services/
│   └── langchain_service.py
├── auth/
│   └── auth.py
├── models/
│   └── query_models.py
├── utils/
│   └── security.py
├── settings.py
└── data/
    └── employee_information.csv
```

### Directory and File Descriptions

- **agents/**: Contains all the agent classes.
  - **agent.py**: Base class for all agents.
  - **greeting_agent.py**: Greeting agent class.
  - **identification_agent.py**: Identification agent class.
  - **investigation_agent.py**: Investigation agent class.
  - **summarization_agent.py**: Summarization agent class.
  - **recommendation_agent.py**: Recommendation agent class.
  - **validation_agent.py**: Validation agent class.

- **state_tracker/**: Contains the state tracker class.
  - **state_tracker.py**: Manages the investigation state.

- **main.py**: Main script to run the chatbot.
- **requirements.txt**: Lists all required Python packages.

- **Dockerfile**: Docker configuration file for containerizing the application.
- **.env**: Environment variables file.
- **routers/**: Contains the router for handling API requests related to the LangChain agent.
  - **query_router.py**: Router for handling queries.
- **services/**: Contains service classes.
  - **langchain_service.py**: Service class to interact with the LangChain agent and the pandas DataFrame.
- **auth/**: Handles HTTP Basic Authentication.
  - **auth.py**: Authentication module.
- **models/**: Contains Pydantic models for request and response validation.
  - **query_models.py**: Query models.
- **utils/**: Utility functions.
  - **security.py**: Utility functions for password hashing and verification.
- **settings.py**: Loads and manages environment variables from the `.env` file.
- **data/**: Directory for data files.
  - **employee_information.csv**: CSV file containing employee information.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/raed1337/RAG_bot.git
   cd RAG_bot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the root directory with the following content:
   ```env
   ALICE_PASSWORD_HASH=...
   BOB_PASSWORD_HASH=...
   API_KEY=...
   FILE_PATH=data/employee_information.csv
   ```

## Running the Application

### Using Docker

1. **Build the Docker Image**:
   ```bash
   docker build -t chatbot_project .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run -d -p 8000:8000 --name chatbot_project chatbot_project
   ```

### Locally

1. **Run the Application**:
   ```bash
   uvicorn server:app --host 0.0.0.0 --port 8000
   ```

## How It Works

1. **Greeting Agent**: Greets the user and introduces the chatbot as an assistant human resource manager it identify if the user have a general problem or a human resource probelm.
2. **Identification Agent**: Identifies whether the user is asking for general information or reporting a problem.
3. **Investigation Agent**: If a problem is reported, this agent asks a series of questions to understand the issue.
4. **State Tracker**: Tracks the state of the conversation during the investigation, ensuring all necessary questions are asked and answered correctly.
5. **Summarization Agent**: Summarizes the conversation and the identified problem.
6. **Recommendation Agent**: Provides recommendations based on the summarized information.

## Security
- Endpoints are protected with HTTP Basic Authentication.
- Passwords are hashed using bcrypt.

## Usage

You can interact with the API using tools like `curl` or Postman. For example, to query the LangChain agent, you can use:

```bash
curl -X POST "https://localhost:8000/api/query" -H "Content-Type: application/json" -u alice:password -d '{"text": "how many days off do I still have, I am bob?"}'
```

Replace `password` with the appropriate credentials.
