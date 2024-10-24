from typing import List, Optional
from pydantic import BaseModel
from datetime import date
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from database import execute_query, execute_non_query
import mysql.connector
import os
from crud import (
    obtener_todos_productos, crear_producto, obtener_producto_por_id, 
    actualizar_producto, eliminar_producto,
    obtener_todo_inventario, crear_inventario, actualizar_inventario, eliminar_inventario,
    obtener_todas_ventas, crear_venta, actualizar_venta, eliminar_venta,
    obtener_todas_compras, crear_compra, actualizar_compra, eliminar_compra,
    obtener_todos_informes, crear_informe, generar_informe_ventas
)
from models import Producto, Inventario, Venta, Compra, Informe

QUERY_LAST_INSERT_ID = "SELECT LAST_INSERT_ID() as id"

# Crear la aplicación FastAPI
app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost",  # URL del frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Variables de entorno para la base de datos MySQL
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "password")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
MYSQL_DB = os.getenv("MYSQL_DB", "test_db")

# Conexión a MySQL
def get_mysql_conn():
    try:
        conn = mysql.connector.connect(
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            database=MYSQL_DB
        )
        return conn
    except Exception as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Modelo de datos para el usuario
class User(BaseModel):
    username: str
    email: str
    password: str
    full_name: str

# Función para registrar un usuario
def registrar_usuario(user: User):
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to MySQL")

    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, email, password, full_name) VALUES (%s, %s, %s, %s)",
            (user.username, user.email, user.password, user.full_name)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "User registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

# Endpoint para registrar un usuario
@app.post("/register/", response_model=User)
def register_user(user: User):
    return registrar_usuario(user)

# Endpoint de prueba para verificar conexión a MySQL
@app.get("/mysql/products/")
def get_products():
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to MySQL")

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Producto;")  # Cambia 'Producto' según tu esquema de tablas
        products = cursor.fetchall()
        cursor.close()
        conn.close()
        return {"products": products}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

# Endpoint de bienvenida
@app.get("/")
def read_root():
    return {"message": "Welcome to the API with MySQL"}

# Producto routes
@app.get("/productos/", response_model=List[Producto])
def leer_productos():
    return obtener_todos_productos()

@app.post("/productos/", response_model=Producto)
def agregar_producto(producto: Producto):
    return crear_producto(producto)

@app.get("/productos/{id_producto}", response_model=Optional[Producto])
def leer_producto_por_id(id_producto: int):
    return obtener_producto_por_id(id_producto)

@app.put("/productos/{id_producto}", response_model=Optional[Producto])
def modificar_producto(id_producto: int, producto_actualizado: Producto):
    return actualizar_producto(id_producto, producto_actualizado)

@app.delete("/productos/{id_producto}")
def borrar_producto(id_producto: int):
    return eliminar_producto(id_producto)

# Inventario routes
@app.get("/inventario/", response_model=List[Inventario])
def leer_inventario():
    return obtener_todo_inventario()

@app.post("/inventario/", response_model=Inventario)
def agregar_inventario(inventario: Inventario):
    return crear_inventario(inventario)

@app.put("/inventario/{id_inventario}", response_model=Optional[Inventario])
def modificar_inventario(id_inventario: int, inventario_actualizado: Inventario):
    return actualizar_inventario(id_inventario, inventario_actualizado)

@app.delete("/inventario/{id_inventario}")
def borrar_inventario(id_inventario: int):
    return eliminar_inventario(id_inventario)

# Venta routes
@app.get("/ventas/", response_model=List[Venta])
def leer_ventas():
    return obtener_todas_ventas()

@app.post("/ventas/", response_model=Venta)
def agregar_venta(venta: Venta):
    return crear_venta(venta)

@app.put("/ventas/{id_venta}", response_model=Optional[Venta])
def modificar_venta(id_venta: int, venta_actualizada: Venta):
    return actualizar_venta(id_venta, venta_actualizada)

@app.delete("/ventas/{id_venta}")
def borrar_venta(id_venta: int):
    return eliminar_venta(id_venta)

# Compra routes
@app.get("/compras/", response_model=List[Compra])
def leer_compras():
    return obtener_todas_compras()

@app.post("/compras/", response_model=Compra)
def agregar_compra(compra: Compra):
    return crear_compra(compra)

@app.put("/compras/{id_compra}", response_model=Optional[Compra])
def modificar_compra(id_compra: int, compra_actualizada: Compra):
    return actualizar_compra(id_compra, compra_actualizada)

@app.delete("/compras/{id_compra}")
def borrar_compra(id_compra: int):
    return eliminar_compra(id_compra)

# Informe routes
@app.get("/informes/", response_model=List[Informe])
def leer_informes():
    return obtener_todos_informes()

@app.post("/informes/", response_model=Informe)
def agregar_informe(informe: Informe):
    return crear_informe(informe)

@app.post("/informes/ventas/")
def generar_informe_de_ventas(fecha_inicio: date, fecha_fin: date):
    return generar_informe_ventas(fecha_inicio, fecha_fin)
