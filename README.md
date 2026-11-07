# Task Management API

A beginner-friendly Task Management REST API built using **Python and FastAPI**. This project demonstrates the fundamentals of backend development, including HTTP methods, CRUD operations, request validation, and API endpoints.

## Features

- Create new tasks
- Retrieve all tasks
- Retrieve a task by ID
- Update an existing task
- Partially update task details
- Delete a task
- Validate request data using Pydantic
- Handle errors using HTTPException

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

## Project Structure

```text
task-management/
│
├── main.py
├── README.md
└── requirements.txt
```

## Installation and Setup

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**2. Navigate to the project directory**

```bash
cd task-management
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment**

Windows:

```bash
venv\Scripts\activate
```

**5. Install dependencies**

```bash
pip install fastapi uvicorn
```

**6. Run the application**

```bash
uvicorn main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/tasks` | Create a task |
| GET | `/tasks` | Retrieve all tasks |
| GET | `/tasks/{task_id}` | Retrieve a task by ID |
| PUT | `/tasks/{task_id}` | Update an entire task |
| PATCH | `/tasks/{task_id}` | Update selected task fields |
| DELETE | `/tasks/{task_id}` | Delete a task |

## API Documentation

After starting the server, open:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

You can test all API endpoints directly through Swagger UI.

## Learning Outcomes

Through this project, I practiced:

- Understanding HTTP methods and REST API fundamentals
- Building API routes using FastAPI
- Working with Python lists and dictionaries
- Using Pydantic models for request validation
- Implementing CRUD operations
- Handling errors and HTTP status codes
- Understanding the difference between PUT and PATCH

## Future Improvements

- Integrate MySQL database
- Implement user authentication
- Add pagination and filtering
- Organize the application using FastAPI routers
- Add automated tests

---

**Note:** This project currently uses in-memory storage (Python lists). Data will reset when the application restarts.

## Author

Built as a hands-on project while learning Python backend development and FastAPI.
 
 
