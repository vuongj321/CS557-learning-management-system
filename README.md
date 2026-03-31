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
