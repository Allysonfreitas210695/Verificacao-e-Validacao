## Step-by-step guide to set up the project

### 1. Create a Virtual Environment:

```bash
  python -m venv venv
```

### 2. Activate the Virtual Environment:

```bash
  source venv/bin/activate
```

### 3. Install Dependencies from requirements.txt:

```bash
  pip install -r requirements.txt
```

### 4. Create Migrations for the Models:

```bash
  python3 manage.py makemigrations
```

### 5. Apply Migrations to the Database:

```bash
  python3 manage.py migrate
```

### 6. Create a Superuser:

```bash
  python3 manage.py createsuperuser
```

### 7. Run the Development Server:

```bash
  python3 manage.py runserver
```

### 7. Run tests for the core repositories and services layer

```bash
  python manage.py test core.tests.services
```

```bash
  python manage.py test core.tests.repositories
```
