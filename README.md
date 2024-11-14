### Flask with Postgres

This README provides step-by-step instructions to set up a Flask project with PostgreSQL integration

### Requirements (Download and Install)

- Python 3
- PostgreSQL

### environment variables

for example:

```
DB_HOST = localhost
DB_PORT = 5432
DB_NAME = your_db_name
DB_USER = postgres
DB_PASSWORD = yoursecretpassword
```

## Installation

### Step 1: Download and Install Python

Download and install Python from [Python's official website](https://www.python.org/downloads/). Ensure that Python is added to your PATH during installation.

### Step 2: Set Up a Virtual Environment

To isolate dependencies, it's recommended to set up a virtual environment.

1. **Install `virtualenv`**:

   ```bash
   pip install virtualenv
   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m virtualenv venv
   ```

3. **Activate the Virtual Environment**:
   - On **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

### Step 3: Install Flask in the Virtual Environment

Once the virtual environment is active, install Flask:

```bash
pip install flask
```

## Step 4: Install Required Packages

Add all required packages to `requirements.txt`, then install them by running:

```bash
pip install -r requirements.txt
```

## Step 5: Set Up SQLAlchemy, psycopg2 for Database Configuration

Configure SQLAlchemy and psycopg2 to manage database interactions for postgresql

## Database Configuration

Create a database in postgresql and run:

```sql
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY NOT NULL,
  name VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  role VARCHAR(255) NOT NULL DEFAULT 'user',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

## Running the Application

Run the project with cmd:

```bash
flask run || python app.py
```
