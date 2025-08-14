## Django Starter Setup

Follow these steps to set up and run your Django project:

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start a New Django Project

```bash
django-admin startproject core .
```

### 3. Run the Development Server

```bash
python manage.py runserver
```

### 4. Apply Initial Database Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser for the Admin Panel

```bash
python manage.py createsuperuser
```