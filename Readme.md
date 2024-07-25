# Django Authentication Project(WhatBytes - Assignment)
WhatBytes Django Assignment:
A Django project with user authentication features including user sign-up, login, logout, password reset, profile management, and email functionality.

## Features

- User Sign-Up
- User Login
- User Logout
- Password Reset
- Profile Management
- Email Functionality

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- virtualenv (Recommended)

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/Yatharth2609/Django_Auth_WhatBytes.git
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:

    Create a `.env` file in the root of your project and add the following variables:

    ```env
    DJANGO_SECRET_KEY=your-secret-key
    DJANGO_DEBUG=True
    DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=your_db_host
    DB_PORT=your_db_port
    ```

5. Apply the migrations:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

8. Open your browser and go to `http://127.0.0.1:8000/` to see your project running.

## Usage

- Sign up as a new user.
- Log in with your credentials.
- Access and edit your profile.
- Reset your password if necessary.

