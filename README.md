# Learning Management System

A Django-based learning management system.

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/vuongj321/CS557-learning-management-system.git
   cd learning-management-system
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## Setting up the MySQL database

1. **Create database and user**

   ```sql
   CREATE DATABASE lms_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   CREATE USER 'lms_user'@'localhost' IDENTIFIED BY '<your_password>'; -- replace <your_password> with a secure password
   GRANT ALL PRIVILEGES ON lms_db.* TO 'lms_user'@'localhost'; -- This is only for local development
   FLUSH PRIVILEGES;
   ```

2. **Update `settings.py`**
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'lms_db',
           'USER': 'lms_user',
           'PASSWORD': '<your_password>',  # Replace <your_password> with the same password used in the SQL command
           'HOST': 'localhost',            # Again, only for local development
           'PORT': '3306',
       }
   }
   ```

3. **Be sure that the MySQL client library is installed**

   ```bash
   pip install mysqlclient
   ```

   Or

   ```bash
   pip install -r requirements.txt
   ```

