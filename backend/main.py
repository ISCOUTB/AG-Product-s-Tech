from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from datetime import date
from fastapi.middleware.cors import CORSMiddleware
from database import get_mysql_conn, execute_query, execute_non_query
from crud import (
    obtener_todos_usuarios, crear_usuario, obtener_usuario_por_id, 
    actualizar_usuario, eliminar_usuario, obtener_todos_productos, 
    crear_producto, obtener_producto_por_id, actualizar_producto, 
    eliminar_producto, obtener_todo_inventario, obtener_inventario_por_id, 
    crear_inventario, actualizar_inventario, eliminar_inventario, 
    obtener_todas_ventas, crear_venta, obtener_venta_por_id, actualizar_venta, 
    eliminar_venta, obtener_todas_compras, crear_compra, obtener_compra_por_id, 
    actualizar_compra, eliminar_compra, obtener_todos_informes, obtener_informe_por_id,
    crear_informe, actualizar_informe, eliminar_informe, generar_informe_ventas
)
from models import User, LoginData, Producto, Inventario, Venta, Compra, Informe

QUERY_LAST_INSERT_ID = "SELECT LAST_INSERT_ID() as id"

# Crear la aplicación FastAPI
app = FastAPI()

# Configuración de CORS
origins = [
    "http://127.0.0.1:2024",  # URL del frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint de bienvenida
@app.get("/")
def read_root():
    return {"message": "Welcome to the API with MySQL"}

# Endpoint para registrar un usuario
@app.post("/register/")
def register_user(user: User):
    query = "INSERT INTO users (nombre_completo, nick, email, contrasena) VALUES (%s, %s, %s, %s)"
    try:
        execute_non_query(query, (user.full_name, user.username, user.email, user.password))
        return {"message": "User registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

@app.post("/login/")
def login(data: LoginData):
    query = "SELECT * FROM users WHERE email = %s AND contrasena = %s"
    try:
        user = execute_query(query, (data.email, data.password))
        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return {"message": "Login successful", "user": user}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

# Endpoint de prueba para verificar conexión a MySQL
@app.get("/mysql/products/")
def test_mysql_connection():
    conn = get_mysql_conn()
    if conn:
        conn.close()
        return {"message": "Conexión exitosa a la base de datos"}
    else:
        raise HTTPException(status_code=500, detail="No se pudo conectar a la base de datos")

# Usuario routes
@app.get("/usuarios/", response_model=List[User])
def obtener_usuarios():
    return obtener_todos_usuarios()

@app.post("/usuarios/", response_model=User)
def crear_usuario(usuario: User):
    return crear_usuario(usuario)

@app.get("/usuarios/{id_usuario}", response_model=User)
def obtener_usuario(id_usuario: int):
    usuario = obtener_usuario_por_id(id_usuario)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@app.put("/usuarios/{id_usuario}", response_model=User)
def actualizar_usuario(id_usuario: int, usuario_actualizado: User):
    usuario = actualizar_usuario(id_usuario, usuario_actualizado)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@app.delete("/usuarios/{id_usuario}")
def eliminar_usuario(id_usuario: int):
    if not eliminar_usuario(id_usuario):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"message": "Usuario eliminado exitosamente"}

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

@app.get("/inventario/{id_inventario}", response_model=Inventario)
def obtener_inventario(id_inventario: int):
    inventario = obtener_inventario_por_id(id_inventario)
    if inventario is None:
        raise HTTPException(status_code=404, detail="Inventario no encontrado")
    return inventario

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

@app.get("/ventas/{id_venta}", response_model=Venta)
def obtener_venta(id_venta: int):
    venta = obtener_venta_por_id(id_venta)
    if venta is None:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    return venta

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

@app.get("/compras/{id_compra}", response_model=Compra)
def obtener_compra(id_compra: int):
    compra = obtener_compra_por_id(id_compra)
    if compra is None:
        raise HTTPException(status_code=404, detail="Compra no encontrada")
    return compra

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

@app.get("/informes/{id_informe}", response_model=Informe)
def obtener_informe(id_informe: int):
    informe = obtener_informe_por_id(id_informe)
    if informe is None:
        raise HTTPException(status_code=404, detail="Informe no encontrado")
    return informe

@app.put("/informes/{id_informe}", response_model=Informe)
def actualizar_informe(id_informe: int, informe_actualizado: Informe):
    informe = actualizar_informe(id_informe, informe_actualizado)
    if informe is None:
        raise HTTPException(status_code=404, detail="Informe no encontrado")
    return informe

@app.delete("/informes/{id_informe}")
def eliminar_informe(id_informe: int):
    if not eliminar_informe(id_informe):
        raise HTTPException(status_code=404, detail="Informe no encontrado")
    return {"message": "Informe eliminado exitosamente"}

@app.post("/informes/ventas/")
def generar_informe_de_ventas(fecha_inicio: date, fecha_fin: date):
    return generar_informe_ventas(fecha_inicio, fecha_fin)