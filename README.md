# Task and User Management API

This API allows for the management of tasks and users, enabling functionalities such as creating users, creating tasks, assigning tasks to users, and retrieving tasks and users.

## Table of Contents

- [Installation](#installation)
- [API Endpoints](#api-endpoints)
  - [1. Create a User](#1-create-a-user)
  - [2. Create a Task](#2-create-a-task)
  - [3. Assign Users to a Task](#3-assign-users-to-a-task)
  - [4. Get All Tasks](#4-get-all-tasks)
  - [5. Get Tasks Assigned to a Specific User](#5-get-tasks-assigned-to-a-specific-user)
  - [6. Get All Users](#6-get-all-users)
- [Usage](#usage)
- [Technologies Used](#technologies-used)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Sattyak/JOSHTALKS.git
   cd task_management
   ```

2. **Create a virtual environment**:
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`

3. **Install the required packages**:
   pip install -r requirements.txt

4. **Apply migrations**:
   python manage.py migrate

5. **Run the development server**:
   python manage.py runserver

The API will be accessible at http://127.0.0.1:8000/api/

API Endpoints: 

    1. Create a User
    Endpoint: POST /users/
    Request Body:
    {   
        "name": "edward",
        "email": "edward@emily.com",
        "mobile": "48654651540"
    }
    Response:
    {
        "id": 4,
        "name": "edward",
        "email": "edward@emily.com",
        "mobile": "48654651540"
    }

    2. Create a Task
    Endpoint: POST /tasks/
    Request Body:
    {
        "name": "task3",
        "description": "description for task3",
        "task_type": "Bug"
    }

    Response:
    {
        "id": 5,
        "name": "task3",
        "description": "description for task3"
    }

    3. Assign Users to a Task
    Endpoint: POST /tasks/<task_id>/assign/
    Request Body:
    {
        "user_ids": [4,5]
    }

    Response:
    {
        "message": "Task assigned successfully",
        "assigned_user_ids": [4,5]
    }

    4. Get All Tasks
    Endpoint: GET /tasks/
    Response:
    [
        {
            "id": 4,
            "name": "task1",
            "description": "description for task1",
            "created_at": "2024-10-21T17:51:07.219059Z",
            "task_type": "userStory",
            "completed_at": null,
            "status": "pending",
            "assigned_users": [
                {
                    "id": 3,
                    "name": "Emily",
                    "email": "emily@edward.com",
                    "mobile": "486543210"
                }
            ]
        }
    ]

    5. Get Tasks Assigned to a Specific User
    Endpoint: GET /users/<user_id>/tasks/
    Response:
    [
        {
            "id": 5,
            "name": "task3",
            "description": "description for task3",
            "created_at": "2024-10-21T19:59:53.229945Z",
            "task_type": "Bug",
            "completed_at": null,
            "status": "pending",
            "assigned_users": [
                {
                    "id": 4,
                    "name": "edward",
                    "email": "edward@emily.com",
                    "mobile": "48654651540"
                }
            ]
        }
    ]

    6. Get All Users
    Endpoint: GET /users/
    Response:
    [
        {
            "id": 1,
            "name": "Sattyak",
            "email": "sattyak@testing.com",
            "mobile": "9876543210"
        },
        {
            "id": 2,
            "name": "Sarma",
            "email": "sarma@testing.com",
            "mobile": "4566543210"
        },
        {
            "id": 3,
            "name": "Emily",
            "email": "emily@edward.com",
            "mobile": "486543210"
        },
        {
            "id": 4,
            "name": "edward",
            "email": "edward@emily.com",
            "mobile": "48654651540"
        }
    ]

Usage:
- After installing and running the server, use a tool like Postman or cURL to interact with the API.

Technologies Used:
- Python 3.10
- Django REST Framework
- Postman (for API testing)

