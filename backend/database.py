import mysql.connector
from mysql.connector import Error
import os

# Definir las variables de entorno directamente en el código
os.environ['DB_HOST'] = '127.0.0.1'
os.environ['DB_PORT'] = '3302'
os.environ['DB_NAME'] = 'productstech_db'
os.environ['DB_USER'] = 'root'
os.environ['DB_PASSWORD'] = 'rootpassword'


def get_mysql_conn():
    """Establece una conexión a la base de datos MySQL."""
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos MySQL")
            return connection
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

def execute_query(query, params=None):
    """Ejecuta una consulta SELECT y devuelve los resultados."""
    connection = get_mysql_conn()
    if connection is None:
        return None
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params)
        results = cursor.fetchall()
        return results
    except Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def execute_non_query(query, params=None):
    """Ejecuta una consulta INSERT, UPDATE o DELETE."""
    connection = get_mysql_conn()
    if connection is None:
        return False
    try:
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        return True
    except Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
