# Django Home Security System

## Overview
This Django project allows for the creation and management of sensors. The project includes endpoints to create sensors, retrieve sensor lists, trigger actions, and log intruder attempts.

## Prerequisites
- Python 3.x
- Django 3.x or higher
- Django REST framework

## Installation

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## API Endpoints

### 1. Create/Get Sensors
- **URL:** `http://<your-ip-address>:8000/sensor/create-get-sensor`
- **Method:** GET / POST

#### Get Sensors
- **Description:** Retrieve the list of all sensors.
- **Response:**
    ```json
    [
        {
            "id": "1fad666a-7e2e-4d0a-ad95-b9bc1ca2a379",
            "pir": "PIR1",
            "status": 0,
            "created_at": "2024-07-11T03:38:20.535343Z"
        },
        {
            "id": "a8a145ce-f441-4c5a-8d99-23013423cc77",
            "pir": "PIR2",
            "status": 0,
            "created_at": "2024-07-11T03:38:20.542303Z"
        },
        {
            "id": "afa99881-95d0-4aa2-bbee-149f7d0cf68f",
            "pir": "PIR3",
            "status": 0,
            "created_at": "2024-07-11T03:38:20.548041Z"
        },
        {
            "id": "364de47b-240f-4709-a726-494663be8e1d",
            "pir": "PIR4",
            "status": 0,
            "created_at": "2024-07-11T03:38:20.555047Z"
        }
    ]
    ```

#### Create Sensor
- **Description:** Automatically create a new sensor.
- **Response:** Newly created sensor object.

### 2. Trigger Action
- **URL:** `http://<your-ip-address>:8000/sensor/trigger-action`
- **Method:** POST
- **Request Body:**
    ```json
    {
        "status": 1,
        "PIR": "PIR1"
    }
    ```
- **Response:**
    - If sensor is not found:
        ```json
        {"send": False, "error": "Sensor not found"}
        ```
    - If action is successfully triggered:
        ```json
        {"send": True}
        ```

### 3. Create/Get Intruder Attempt
- **URL:** `http://<your-ip-address>:8000/sensor/create-get-intruder-attempt`
- **Method:** GET / POST

#### Get Intruder Attempts
- **Description:** Retrieve the list of all intruder attempts.
- **Response:**
    ```json
    [
        {
            "id": "1fad666a-7e2e-4d0a-ad95-b9bc1ca2a379",
            "pir": "PIR1",
            "status": 1,
            "created_at": "2024-07-11T03:38:20.535343Z"
        },
        {
            "id": "a8a145ce-f441-4c5a-8d99-23013423cc77",
            "pir": "PIR1",
            "status": 1,
            "created_at": "2024-07-11T03:38:20.542303Z"
        },
        {
            "id": "a8a145ce-f441-4c5a-8d99-23013423cc77",
            "pir": "PIR3",
            "status": 1,
            "created_at": "2024-07-11T03:38:20.542303Z"
        },
        ...
    ]
    ```

#### Create Intruder Attempt
- **Request Body:**
    ```json
    {
        "status": 1,
        "PIR": "PIR1"
    }
    ```
- **Response:**
    - If sensor is not found:
        ```json
        {"send": False, "error": "Sensor not found"}
        ```
    - If attempt is successfully logged:
        ```json
        {"send": True}
        ```

## Note
- Customize the IP address as per your configuration.
- Ensure Django server is running on the specified IP address.

## Additional Information
- For more information on Django, visit [Django Documentation](https://docs.djangoproject.com/en/stable/).
- For more information on Django REST framework, visit [Django REST framework Documentation](https://www.django-rest-framework.org/).