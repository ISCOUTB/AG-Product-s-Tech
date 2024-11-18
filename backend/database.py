import mysql.connector
from mysql.connector import Error
import os

# Variables de entorno para la base de datos MySQL
MYSQL_USER = os.getenv("DB_USER", "root")
MYSQL_PASSWORD = os.getenv("DB_PASSWORD", "rootpassword")
MYSQL_HOST = os.getenv("DB_HOST", "127.0.0.1")
MYSQL_PORT = int(os.getenv("DB_PORT", 3306))
MYSQL_DB = os.getenv("DB_NAME", "productstech_db")

def get_mysql_conn():
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB,
            port=MYSQL_PORT
        )
        if conn.is_connected():
            print("Conexión exitosa a la base de datos")
            return conn
        else:
            print("No se pudo conectar a la base de datos")
            return None
    except Error as e:
        print(f"Error: {e}")
        return None

def execute_query(query: str, params: tuple = ()):
    try:
        connection = get_mysql_conn()
        if connection is None:
            raise Exception("Failed to connect to the database")
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def execute_non_query(query: str, params: tuple = ()):
    try:
        connection = get_mysql_conn()
        if connection is None:
            raise Exception("Failed to connect to the database")
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def execute_scalar(query: str, params: tuple = ()):
    try:
        connection = get_mysql_conn()
        if connection is None:
            raise Exception("Failed to connect to the database")
        cursor = connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        return result[0] if result else None
    except Error as e:
        print(f"Error: {e}")
        return None
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()