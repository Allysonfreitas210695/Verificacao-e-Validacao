## Step-by-Step Guide for Setting Up a Django Project

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
  source pip install -r requirements.txt
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
