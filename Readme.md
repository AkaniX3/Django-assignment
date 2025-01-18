# Django Referral System

This project is a Django-based web application that includes features for user registration, login, and referral management.

## Features

- **User Registration:** Allows users to sign up with mandatory fields like email, name, mobile number, city, and password.
- **User Login:** Authenticates users via email and password.
- **Referral System:** Returns a list of users who registered using a given referral code.

## Prerequisites

- Python 3.8 or later
- Django 3.x
- PostgreSQL (or use SQLite for development)

## Setup Instructions

Follow these steps to set up the project locally.

### 1. Clone the Repository

Clone the repository to your local machine.

```bash
git clone https://github.com/AkaniX3/Django-assignment.git
cd Django-assignment
```

### 2. Create a Virtual Environment

Create and activate a virtual environment for the project.

```bash
# For Linux/macOS
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

Install the necessary Python packages using `pip`.

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

You need to create a `.env` file in the project root to store sensitive information like the Django `SECRET_KEY`, `DATABASE_URL`, and `WEB_CONCURRENCY`. The `.env` file should contain the following:

```env
SECRET_KEY='your-django-secret-key'
DATABASE_URL='your-database-url'  # This can be the Render URL or a local PostgreSQL URL
WEB_CONCURRENCY=2  # Number of workers for your web server
```

### 5. Modify Database Settings (Optional)

If you're not using Render for the database, you'll need to modify the `DATABASES` section in `settings.py`. Look for this section:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Change it accordingly if you're using SQLite or another database.

### 6. Run Database Migrations

Apply the migrations to create the necessary database tables.

```bash
python manage.py migrate
```

### 7. Create a Superuser (Optional)

If you want to log in to the Django admin interface, create a superuser.

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

Start the Django development server to run the application locally.

```bash
python manage.py runserver
```

You should now be able to access the application at:

```
http://127.0.0.1:8000/
```

## How to Use the Application

- **Home Page:** Navigate to the home page, where you can choose to go to the register, login, or referral pages.
- **Register:** Enter the necessary details such as email, name, mobile number, city, and password. If you have a referral code, you can include it here.
- **Login:** Use your registered email and password to log in. If successful, you'll receive your user ID and referral code.
- **Referral:** Enter your referral code to see a list of users who signed up using your referral. It shows the name, email ID, and registration date/time of the users.

## Deployment on Render

The application has been deployed on Render: [Django Referral System](https://akani-django-assignment.onrender.com/).

### Note:
The deployment is on a free plan, so after a period of inactivity, the service may spin down. The first request after a spin-down may take 5-15 minutes to activate the service.


ty 🍞✨