from typing import List, Optional
from fastapi import FastAPI, HTTPException, status, Query
from datetime import date, datetime
from fastapi.middleware.cors import CORSMiddleware
from database import get_mysql_conn, execute_query, execute_non_query, execute_scalar
from models import Usuario, LoginData, Producto, Inventario, Venta, Compra, Informe, Marca, Categoria, Proveedor, Cliente, Pedido

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

@app.post("/login/")
def login(data: LoginData):
    query = "SELECT * FROM usuarios WHERE email = %s AND contrasena = %s"
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
@app.get("/usuarios/")
def obtener_todos_usuarios():
    query = "SELECT * FROM usuarios"
    try:
        usuarios = execute_query(query)
        return usuarios
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

@app.post("/usuarios/")
def crear_usuario(user: Usuario):
    check_query = "SELECT COUNT(*) FROM usuarios WHERE email = %s"
    insert_query = "INSERT INTO usuarios (nombre_completo, nick, email, contrasena) VALUES (%s, %s, %s, %s)"
    try:
        count = execute_scalar(check_query, (user.email,))
        if count > 0:
            raise HTTPException(status_code=400, detail="El email ya está registrado")
        execute_non_query(insert_query, (user.nombre_completo, user.nick, user.email, user.contrasena))
        return {"message": "Usuario registrado exitosamente"}
    except Exception as e:
        print(f"Error al registrar usuario: {e}")
        raise HTTPException(status_code=500, detail=f"Error al registrar usuario: {e}")


@app.get("/usuarios/{id_usuario}")
def obtener_usuario_por_id(id_usuario: int):
    query = "SELECT * FROM usuarios WHERE Id_usuario = %s"
    try:
        usuario = execute_query(query, (id_usuario,))
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return usuario[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener usuario: {e}")


@app.put("/usuarios/{id_usuario}")
def actualizar_usuario(id_usuario: int, usuario_actualizado: Usuario):
    query = """
        UPDATE usuarios
        SET nombre_completo = %s, nick = %s, email = %s, contrasena = %s
        WHERE Id_usuario = %s
    """
    try:
        execute_non_query(query, (
            usuario_actualizado.nombre_completo,
            usuario_actualizado.nick,
            usuario_actualizado.email,
            usuario_actualizado.contrasena,
            id_usuario
        ))
        return usuario_actualizado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

@app.delete("/usuarios/{id_usuario}")
def eliminar_usuario(id_usuario: int):
    query_check = "SELECT COUNT(*) FROM usuarios WHERE Id_usuario = %s"
    query_delete = "DELETE FROM usuarios WHERE Id_usuario = %s"
    try:
        count = execute_scalar(query_check, (id_usuario,))
        if count == 0:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        execute_non_query(query_delete, (id_usuario,))
        return {"message": "Usuario eliminado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")


# Producto routes
@app.get("/productos/")
def obtener_todos_productos():
    query = "SELECT * FROM productos"
    try:
        productos = execute_query(query)
        return productos
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

@app.post("/productos/")
def crear_producto(producto: Producto):
    query = "INSERT INTO productos (Nombre, Categoria, Descripcion, Precio, fecha_lanzamineto, Especificaciones, Id_Marca) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    try:
        execute_non_query(query, (producto.Nombre, producto.Categoria, producto.Descripcion, producto.Precio, producto.fecha_lanzamineto, producto.Especificaciones, producto.Id_Marca))
        return {"message": "Producto registrado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

@app.get("/productos/{id_producto}")
def obtener_producto_por_id(id_producto: int):
    query = "SELECT * FROM productos WHERE Id_producto = %s"
    try:
        producto = execute_query(query, (id_producto,))
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        return producto[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener producto: {e}")

@app.put("/productos/{id_producto}")
def actualizar_producto(id_producto: int, producto_actualizado: Producto):
    query = """
        UPDATE productos
        SET Nombre = %s, Categoria = %s, Descripcion = %s, Precio = %s, fecha_lanzamineto = %s, Especificaciones = %s, Id_Marca = %s
        WHERE Id_producto = %s
    """
    try:
        execute_non_query(query, (
            producto_actualizado.Nombre,
            producto_actualizado.Categoria,
            producto_actualizado.Descripcion,
            producto_actualizado.Precio,
            producto_actualizado.fecha_lanzamineto,
            producto_actualizado.Especificaciones,
            producto_actualizado.Id_Marca,
            id_producto
        ))
        return producto_actualizado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

@app.delete("/productos/{id_producto}")
def eliminar_producto(id_producto: int):
    query_check = "SELECT COUNT(*) FROM productos WHERE Id_producto = %s"
    query_delete = "DELETE FROM productos WHERE Id_producto = %s"
    try:
        count = execute_scalar(query_check, (id_producto,))
        if count == 0:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        execute_non_query(query_delete, (id_producto,))
        return {"message": "Producto eliminado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

# Inventario routes
@app.get("/inventario/")
def obtener_todo_inventario():
    query = "SELECT * FROM inventario"
    try:
        inventario = execute_query(query)
        return inventario
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

@app.post("/inventario/")
def crear_inventario(inventario: Inventario):
    query = "INSERT INTO inventario (Id_producto, cantidad_stock, Ubicacion_producto) VALUES (%s, %s, %s)"
    try:
        execute_non_query(query, (inventario.Id_producto, inventario.cantidad_stock, inventario.Ubicacion_producto))
        return {"message": "Inventario registrado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

@app.get("/inventario/{id_inventario}")
def obtener_inventario_por_id(id_inventario: int):
    query = "SELECT * FROM inventario WHERE Id_inventario = %s"
    try:
        inventario = execute_query(query, (id_inventario,))
        if not inventario:
            raise HTTPException(status_code=404, detail="Inventario no encontrado")
        return inventario[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener inventario: {e}")

@app.put("/inventario/{id_inventario}")
def actualizar_inventario(id_inventario: int, inventario_actualizado: Inventario):
    query = """
        UPDATE inventario
        SET Id_producto = %s, cantidad_stock = %s, Ubicacion_producto = %s
        WHERE Id_inventario = %s
    """
    try:
        execute_non_query(query, (
            inventario_actualizado.Id_producto,
            inventario_actualizado.cantidad_stock,
            inventario_actualizado.Ubicacion_producto,
            id_inventario
        ))
        return inventario_actualizado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

@app.delete("/inventario/{id_inventario}")
def eliminar_inventario(id_inventario: int):
    query_check = "SELECT COUNT(*) FROM inventario WHERE Id_inventario = %s"
    query_delete = "DELETE FROM inventario WHERE Id_inventario = %s"
    try:
        count = execute_scalar(query_check, (id_inventario,))
        if count == 0:
            raise HTTPException(status_code=404, detail="Inventario no encontrado")
        execute_non_query(query_delete, (id_inventario,))
        return {"message": "Inventario eliminado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

# Venta routes
@app.get("/ventas/")
def obtener_todas_ventas():
    query = "SELECT * FROM ventas"
    try:
        ventas = execute_query(query)
        return ventas
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

@app.post("/ventas/")
def crear_venta(venta: Venta):
    query = "INSERT INTO ventas (Id_producto, Cantidad, Fecha) VALUES (%s, %s, %s)"
    try:
        execute_non_query(query, (venta.Id_producto, venta.Cantidad, venta.Fecha))
        return {"message": "Venta registrada exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

@app.get("/ventas/{id_venta}")
def obtener_venta_por_id(id_venta: int):
    query = "SELECT * FROM ventas WHERE Id_venta = %s"
    try:
        venta = execute_query(query, (id_venta,))
        if not venta:
            raise HTTPException(status_code=404, detail="Venta no encontrada")
        return venta[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener venta: {e}")

@app.put("/ventas/{id_venta}")
def actualizar_venta(id_venta: int, venta_actualizada: Venta):
    query = """
        UPDATE ventas
        SET Id_producto = %s, Cantidad = %s, Fecha = %s
        WHERE Id_venta = %s
    """
    try:
        execute_non_query(query, (
            venta_actualizada.Id_producto,
            venta_actualizada.Cantidad,
            venta_actualizada.Fecha,
            id_venta
        ))
        return venta_actualizada
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

@app.delete("/ventas/{id_venta}")
def eliminar_venta(id_venta: int):
    query_check = "SELECT COUNT(*) FROM ventas WHERE Id_venta = %s"
    query_delete = "DELETE FROM ventas WHERE Id_venta = %s"
    try:
        count = execute_scalar(query_check, (id_venta,))
        if count == 0:
            raise HTTPException(status_code=404, detail="Venta no encontrada")
        execute_non_query(query_delete, (id_venta,))
        return {"message": "Venta eliminada exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

# Compra routes
@app.get("/compras/")
def obtener_todas_compras():
    query = "SELECT * FROM compras"
    try:
        compras = execute_query(query)
        return compras
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

@app.post("/compras/")
def crear_compra(compra: Compra):
    query = "INSERT INTO compras (Id_producto, Cantidad, Fecha) VALUES (%s, %s, %s)"
    try:
        execute_non_query(query, (compra.Id_producto, compra.Cantidad, compra.Fecha))
        return {"message": "Compra registrada exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

@app.get("/compras/{id_compra}")
def obtener_compra_por_id(id_compra: int):
    query = "SELECT * FROM compras WHERE Id_compra = %s"
    try:
        compra = execute_query(query, (id_compra,))
        if not compra:
            raise HTTPException(status_code=404, detail="Compra no encontrada")
        return compra[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener compra: {e}")

@app.put("/compras/{id_compra}")
def actualizar_compra(id_compra: int, compra_actualizada: Compra):
    query = """
        UPDATE compras
        SET Id_producto = %s, Cantidad = %s, Fecha = %s
        WHERE Id_compra = %s
    """
    try:
        execute_non_query(query, (
            compra_actualizada.Id_producto,
            compra_actualizada.Cantidad,
            compra_actualizada.Fecha,
            id_compra
        ))
        return compra_actualizada
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

@app.delete("/compras/{id_compra}")
def eliminar_compra(id_compra: int):
    query_check = "SELECT COUNT(*) FROM compras WHERE Id_compra = %s"
    query_delete = "DELETE FROM compras WHERE Id_compra = %s"
    try:
        count = execute_scalar(query_check, (id_compra,))
        if count == 0:
            raise HTTPException(status_code=404, detail="Compra no encontrada")
        execute_non_query(query_delete, (id_compra,))
        return {"message": "Compra eliminada exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

# Informe routes
@app.get("/informes/")
def obtener_todos_informes():
    query = "SELECT * FROM informes"
    try:
        informes = execute_query(query)
        return informes
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

@app.post("/informes/")
def crear_informe(informe: Informe):
    query = "INSERT INTO informes (Titulo, Contenido, Fecha) VALUES (%s, %s, %s)"
    try:
        execute_non_query(query, (informe.Titulo, informe.Contenido, informe.Fecha))
        return {"message": "Informe registrado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

@app.get("/informes/{id_informe}")
def obtener_informe_por_id(id_informe: int):
    query = "SELECT * FROM informes WHERE Id_informe = %s"
    try:
        informe = execute_query(query, (id_informe,))
        if not informe:
            raise HTTPException(status_code=404, detail="Informe no encontrado")
        return informe[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener informe: {e}")

@app.put("/informes/{id_informe}")
def actualizar_informe(id_informe: int, informe_actualizado: Informe):
    query = """
        UPDATE informes
        SET Titulo = %s, Contenido = %s, Fecha = %s
        WHERE Id_informe = %s
    """
    try:
        execute_non_query(query, (
            informe_actualizado.Titulo,
            informe_actualizado.Contenido,
            informe_actualizado.Fecha,
            id_informe
        ))
        return informe_actualizado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

@app.delete("/informes/{id_informe}")
def eliminar_informe(id_informe: int):
    query_check = "SELECT COUNT(*) FROM informes WHERE Id_informe = %s"
    query_delete = "DELETE FROM informes WHERE Id_informe = %s"
    try:
        count = execute_scalar(query_check, (id_informe,))
        if count == 0:
            raise HTTPException(status_code=404, detail="Informe no encontrado")
        execute_non_query(query_delete, (id_informe,))
        return {"message": "Informe eliminado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")

@app.post("/informes/ventas/")
def generar_informe_de_ventas(fecha_inicio: date = Query(...), fecha_fin: date = Query(...)):
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to MySQL")

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM ventas WHERE Fecha BETWEEN %s AND %s", 
            (fecha_inicio, fecha_fin)
        )
        ventas_periodo = cursor.fetchall()
        total_ventas = sum(row["Cantidad"] for row in ventas_periodo)
        descripcion = f"Informe de ventas del {fecha_inicio} al {fecha_fin}. Total de ventas: {total_ventas}"
        
        nuevo_informe = Informe(
            Titulo="Informe de Ventas",
            Contenido=descripcion,
            Fecha=datetime.today().date()
        )
        
        # Insertar el informe en la base de datos
        cursor.execute(
            "INSERT INTO informes (Titulo, Contenido, Fecha) VALUES (%s, %s, %s)",
            (nuevo_informe.Titulo, nuevo_informe.Contenido, nuevo_informe.Fecha)
        )
        conn.commit()
        nuevo_informe.Id_informe = cursor.lastrowid
        return nuevo_informe
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al generar el informe: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Marcas routes
@app.get("/marcas/")
def obtener_todas_marcas():
    query = "SELECT * FROM marcas"
    try:
        marcas = execute_query(query)
        return marcas
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")
    
@app.post("/marcas/")
def crear_marca(marca: Marca):
    query = "INSERT INTO marcas (nombre, pais_origen) VALUES (%s, %s)"
    try:
        execute_non_query(query, (marca.nombre, marca.pais_origen))
        return {"message": "Marca registrada exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")
    
@app.get("/marcas/{id_marca}")
def obtener_marca_por_id(id_marca: int):
    query = "SELECT * FROM marcas WHERE Id_marca = %s"
    try:
        marca = execute_query(query, (id_marca,))
        if not marca:
            raise HTTPException(status_code=404, detail="Marca no encontrada")
        return marca[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener marca: {e}")
    
@app.put("/marcas/{id_marca}")
def actualizar_marca(id_marca: int, marca_actualizada: Marca):
    query = """
        UPDATE marcas
        SET nombre = %s, pais_origen = %s
        WHERE Id_marca = %s
    """
    try:
        execute_non_query(query, (
            marca_actualizada.nombre,
            marca_actualizada.pais_origen,
            id_marca
        ))
        return marca_actualizada
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")
    
@app.delete("/marcas/{id_marca}")
def eliminar_marca(id_marca: int):
    query_check = "SELECT COUNT(*) FROM marcas WHERE Id_marca = %s"
    query_delete = "DELETE FROM marcas WHERE Id_marca = %s"
    try:
        count = execute_scalar(query_check, (id_marca,))
        if count == 0:
            raise HTTPException(status_code=404, detail="Marca no encontrada")
        execute_non_query(query_delete, (id_marca,))
        return {"message": "Marca eliminada exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL query failed: {e}")