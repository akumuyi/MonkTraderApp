# MonkTraderApp

MonkTraderApp is a web-app designed to facilitate access to financial markets information and resources for low-income earners and market enthusiasts generally. 

## Features

- *Market Reports*: Traders, financial analyst, technical analyst and the general public can find insightful market analysis and reports on the app.
- *Signal Services*: Signals are posted on the app for trading opportunities on a daily/weekly basis.
- *Education/Mentorship*: Learning materials like videos, images, PDFs and audio notes are also shared regularly for trader development.
- *Custom Authentication*: Secure custom authentication backend.
- *Admin Interface*: Create and manage application content.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default for Django, can be configured to use other databases)
- **Authentication**: Django's built-in authentication system

## Installation

### Prerequisites

- Python 3.10+

### Setup

1. *Create and activate a virtual environment:*
   bash
   ```
   python -m venv your_virtual_environment_name
   source venv/bin/activate   # On Windows use, `your_virtual_environment_name\Scripts\activate`
   ```

2. *Clone the repository:*
   bash
   ```
   git clone https://github.com/akumuyi/MonkTraderApp.git
   ```

3. * Change to git repository*
   bash
   ```
   cd MonkTraderApp/

 *Install dependencies:*
   bash
   ```
   pip install -r requirements.txt
   ```

4. *Set up the Django project:*
   bash
   ```
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser --email=your_email --username=your_username
   python manage.py check
   python manage.py runserver
   ```

  
## Usage

- Log in to the admin panel at http://127.0.0.1:8000/admin/ using your superuser credentials.
- Login or register at http://127.0.0.1:8000/MonkTraderApp/login/

### Admin and User Homepages

- Admin users will be redirected to `homepage1`.
- Regular users will be redirected to `homepage2`.


## Contributing

Contributions are welcomed! Please see [CONTRIBUTING.md](CONTRIBUTING.md) file for more details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Additional Included Files

1. *CONTRIBUTING.md*: Guidelines for contributing to the project.
2. *LICENSE*: The licensing information for the project.
3. *requirements.txt*: List of dependencies required to run the project.
4. *.gitignore*: Specifies files and directories to be ignored by Git.
