# Database operations for the DevOps application

import mysql.connector
import os
from mysql.connector import Error

def get_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', ''),
        database=os.getenv('DB_NAME', 'devops_db')
    )

def init_db():
    conn = None
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS estudiantes (
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                nombre VARCHAR(255) NOT NULL,
                edad INTEGER NOT NULL
            )
        ''')
        conn.commit()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            c.close()
            conn.close()

def create_estudiante(nombre, edad):
    conn = None
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute('INSERT INTO estudiantes (nombre, edad) VALUES (%s, %s)', (nombre, edad))
        conn.commit()
        return c.lastrowid
    except Error as e:
        print(f"Error: {e}")
        return None
    finally:
        if conn and conn.is_connected():
            c.close()
            conn.close()

def get_all_estudiantes():
    conn = None
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM estudiantes')
        return [{'id': row[0], 'nombre': row[1], 'edad': row[2]} for row in c.fetchall()]
    except Error as e:
        print(f"Error: {e}")
        return []
    finally:
        if conn and conn.is_connected():
            c.close()
            conn.close()

def get_estudiante(id):
    conn = None
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM estudiantes WHERE id = %s', (id,))
        row = c.fetchone()
        return {'id': row[0], 'nombre': row[1], 'edad': row[2]} if row else None
    except Error as e:
        print(f"Error: {e}")
        return None
    finally:
        if conn and conn.is_connected():
            c.close()
            conn.close()

def update_estudiante(id, nombre, edad):
    conn = None
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute('UPDATE estudiantes SET nombre = %s, edad = %s WHERE id = %s', (nombre, edad, id))
        conn.commit()
        return c.rowcount > 0
    except Error as e:
        print(f"Error: {e}")
        return False
    finally:
        if conn and conn.is_connected():
            c.close()
            conn.close()

def delete_estudiante(id):
    conn = None
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute('DELETE FROM estudiantes WHERE id = %s', (id,))
        conn.commit()
        return c.rowcount > 0
    except Error as e:
        print(f"Error: {e}")
        return False
    finally:
        if conn and conn.is_connected():
            c.close()
            conn.close()
