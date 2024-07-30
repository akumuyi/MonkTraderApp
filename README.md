# MonkTraderApp

MonkTraderApp is a web application designed to provide market analysis reports. This application includes user authentication, allowing users to log in and access different features based on their roles (e.g., admin or regular user).

## Features

- User Authentication
  - Login with username and password
  - Error handling for invalid login attempts
- Role-based Access Control
  - Different homepages for admin and regular users
- Market Analysis Reports
  - Access to various market analysis tools and reports

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default for Django, can be configured to use other databases)
- **Authentication**: Django's built-in authentication system

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/MonkTraderApp.git
    cd MonkTraderApp
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

### Login

- Navigate to the login page.
- Enter your username and password.
- If the credentials are incorrect, an error message will be displayed.

### Admin and User Homepages

- Admin users will be redirected to `homepage1`.
- Regular users will be redirected to `homepage2`.

## JavaScript Functionality

The `auth.js` file contains JavaScript code that enhances the user experience on the login page. It handles input focus and blur events to style the labels accordingly.