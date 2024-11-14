from flask import Flask, jsonify, request, send_file
from psycopg2 import connect, extras
from os import environ
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()

app = Flask(__name__)
key = Fernet.generate_key()

host = environ.get('DB_HOST')
database = environ.get('DB_NAME')
name = environ.get('DB_USER')
password = environ.get('DB_PASSWORD')
port = environ.get('DB_PORT')

print(host, database, name, password, port)


def get_db_connection():
    conn = connect(host=host, database=database,
                   user=name, password=password, port=port)
    return conn


@app.get('/api/users')
def get_users():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(users)


@app.post('/api/users')
def create_user():
    try:
        new_user = request.get_json()
        name = new_user['name']
        email = new_user['email']
        password = Fernet(key).encrypt(bytes(new_user['password'], 'utf-8'))
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s) RETURNING *",
                    (name, email, password))
        new_user = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return jsonify(new_user)
    except Exception as error:
        print(error)
        return jsonify({'message': 'An error occurred'}), 500


@app.get('/api/users/<id>')
def get_user(id):
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute("SELECT * FROM users WHERE id = %s", (id,))
        user = cur.fetchone()
        cur.close()
        conn.close()
        if user is None:
            return jsonify({'message': 'User not found'}), 404
        return jsonify(user)
    except Exception as error:
        print(error)
        return jsonify({'message': 'An error occurred'}), 500

@app.put('/api/users/<id>')
def update_user(id):
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)
        new_user = request.get_json()
        name = new_user['name']
        email = new_user['email']
        password = Fernet(key).encrypt(bytes(new_user['password'], 'utf-8'))
        cur.execute("UPDATE users SET name = %s, email = %s, password = %s WHERE id = %s RETURNING *",
                    (name, email, password, id))
        updated_user = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        if updated_user is None:
            return jsonify({'message': 'User not found'}), 404
        return jsonify(updated_user)
    except Exception as error:
        print(error)
        return jsonify({'message': 'An error occurred'}), 500

@app.delete('/api/users/<id>')
def delete_user(id):
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute("DELETE FROM users WHERE id = %s RETURNING *", (id,))
        user = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        if user is None:
            return jsonify({'message': 'User not found'}), 404
        return jsonify(user)
    except Exception as error:
        print(error)
        return jsonify({'message': 'An error occurred'}), 500

@app.get('/')
def home():
    return send_file('static/index.html')


if __name__ == '__main__':
    app.run(debug=True, port=3000)
