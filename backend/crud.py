from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date
from fastapi import HTTPException
from .models import Producto, Inventario, Venta, Compra, Informe
from .database import get_mysql_conn  

# Funciones para Productos
def obtener_todos_productos() -> List[Producto]:
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to SQLite")
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Producto;")
        rows = cursor.fetchall()
        return [Producto(**dict(row)) for row in rows]  # Mapear filas a instancias de Producto
    finally:
        conn.close()

def crear_producto(producto: Producto) -> Producto:
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to SQLite")

    try:
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO Producto (ID_producto, Nombre, Descripcion, categoria, precio, fecha_lanzamiento, especificaciones, ID_marca) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", 
            (producto.ID_producto, producto.Nombre, producto.Descripcion, producto.categoria, producto.precio, 
             producto.fecha_lanzamiento, producto.especificaciones, producto.ID_marca)
        )
        conn.commit()
        return producto
    finally:
        conn.close()

def obtener_producto_por_id(id_producto: int) -> Optional[Producto]:
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to SQLite")
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Producto WHERE ID_producto = ?;", (id_producto,))
        row = cursor.fetchone()
        if row:
            return Producto(**dict(row))
        return None
    finally:
        conn.close()

def actualizar_producto(id_producto: int, producto_actualizado: Producto) -> Optional[Producto]:
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to SQLite")

    try:
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE Producto SET Nombre = ?, Descripcion = ?, categoria = ?, precio = ?, 
            fecha_lanzamiento = ?, especificaciones = ?, ID_marca = ? WHERE ID_producto = ?""",
            (producto_actualizado.Nombre, producto_actualizado.Descripcion, producto_actualizado.categoria, 
             producto_actualizado.precio, producto_actualizado.fecha_lanzamiento, producto_actualizado.especificaciones, 
             producto_actualizado.ID_marca, id_producto)
        )
        conn.commit()
        if cursor.rowcount == 0:
            return None
        return producto_actualizado
    finally:
        conn.close()

def eliminar_producto(id_producto: int) -> bool:
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to SQLite")

    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Producto WHERE ID_producto = ?;", (id_producto,))
        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()

# Funciones para Inventario
def obtener_todo_inventario() -> List[Inventario]:
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to SQLite")
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Inventario;")
        rows = cursor.fetchall()
        return [Inventario(**dict(row)) for row in rows]
    finally:
        conn.close()

def crear_inventario(inventario: Inventario) -> Inventario:
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to SQLite")

    try:
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO Inventario (ID_inventario, ID_producto, cantidad_stock, ubicacion_producto) 
            VALUES (?, ?, ?, ?)""", 
            (inventario.ID_inventario, inventario.ID_producto, inventario.cantidad_stock, inventario.ubicacion_producto)
        )
        conn.commit()
        return inventario
    finally:
        conn.close()

def obtener_inventario_por_id(id_inventario: int) -> Optional[Inventario]:
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to SQLite")

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Inventario WHERE ID_inventario = ?;", (id_inventario,))
        row = cursor.fetchone()
        if row:
            return Inventario(**dict(row))
        return None
    finally:
        conn.close()

def actualizar_inventario(id_inventario: int, inventario_actualizado: Inventario) -> Optional[Inventario]:
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to SQLite")

    try:
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE Inventario SET ID_producto = ?, cantidad_stock = ?, ubicacion_producto = ?
            WHERE ID_inventario = ?""",
            (inventario_actualizado.ID_producto, inventario_actualizado.cantidad_stock, 
             inventario_actualizado.ubicacion_producto, id_inventario)
        )
        conn.commit()
        if cursor.rowcount == 0:
            return None
        return inventario_actualizado
    finally:
        conn.close()

def eliminar_inventario(id_inventario: int) -> bool:
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to SQLite")

    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Inventario WHERE ID_inventario = ?;", (id_inventario,))
        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()

# Funciones para Ventas
def obtener_todas_ventas() -> List[Venta]:
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to SQLite")
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Venta;")
        rows = cursor.fetchall()
        return [Venta(**dict(row)) for row in rows]
    finally:
        conn.close()

def crear_venta(venta: Venta) -> Venta:
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to SQLite")

    try:
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO Venta (ID_venta, ID_producto, cantidad, fecha_venta) 
            VALUES (?, ?, ?, ?)""", 
            (venta.ID_venta, venta.ID_producto, venta.cantidad, venta.fecha_venta)
        )
        conn.commit()
        return venta
    finally:
        conn.close()

def obtener_venta_por_id(id_venta: int) -> Optional[Venta]:
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to SQLite")

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Venta WHERE ID_venta = ?;", (id_venta,))
        row = cursor.fetchone()
        if row:
            return Venta(**dict(row))
        return None
    finally:
        conn.close()

def actualizar_venta(id_venta: int, venta_actualizada: Venta) -> Optional[Venta]:
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to SQLite")

    try:
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE Venta SET ID_producto = ?, cantidad = ?, fecha_venta = ? 
            WHERE ID_venta = ?""",
            (venta_actualizada.ID_producto, venta_actualizada.cantidad, 
             venta_actualizada.fecha_venta, id_venta)
        )
        conn.commit()
        if cursor.rowcount == 0:
            return None
        return venta_actualizada
    finally:
        conn.close()

def eliminar_venta(id_venta: int) -> bool:
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to SQLite")

    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Venta WHERE ID_venta = ?;", (id_venta,))
        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()

# Funciones para Compras
def obtener_todas_compras() -> List[Compra]:
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to SQLite")
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Compra;")
        rows = cursor.fetchall()
        return [Compra(**dict(row)) for row in rows]
    finally:
        conn.close()

def crear_compra(compra: Compra) -> Compra:
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to SQLite")

    try:
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO Compra (ID_compra, ID_producto, cantidad, proveedor, fecha_compra) 
            VALUES (?, ?, ?, ?, ?)""", 
            (compra.ID_compra, compra.ID_producto, compra.cantidad, compra.proveedor, compra.fecha_compra)
        )
        conn.commit()
        return compra
    finally:
        conn.close()

def obtener_compra_por_id(id_compra: int) -> Optional[Compra]:
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to SQLite")

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Compra WHERE ID_compra = ?;", (id_compra,))
        row = cursor.fetchone()
        if row:
            return Compra(**dict(row))
        return None
    finally:
        conn.close()

def actualizar_compra(id_compra: int, compra_actualizada: Compra) -> Optional[Compra]:
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to SQLite")

    try:
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE Compra SET ID_producto = ?, cantidad = ?, proveedor = ?, fecha_compra = ? 
            WHERE ID_compra = ?""",
            (compra_actualizada.ID_producto, compra_actualizada.cantidad, compra_actualizada.proveedor, 
             compra_actualizada.fecha_compra, id_compra)
        )
        conn.commit()
        if cursor.rowcount == 0:
            return None
        return compra_actualizada
    finally:
        conn.close()

def eliminar_compra(id_compra: int) -> bool:
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to SQLite")

    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Compra WHERE ID_compra = ?;", (id_compra,))
        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()

# Funciones para Informes
def obtener_todos_informes() -> List[Informe]:
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to SQLite")
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Informe;")
        rows = cursor.fetchall()
        return [Informe(**dict(row)) for row in rows]
    finally:
        conn.close()

def crear_informe(informe: Informe) -> Informe:
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to SQLite")

    try:
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO Informe (ID_informe, tipo_informe, descripcion, fecha_generacion) 
            VALUES (?, ?, ?, ?)""", 
            (informe.ID_informe, informe.tipo_informe, informe.descripcion, informe.fecha_generacion)
        )
        conn.commit()
        return informe
    finally:
        conn.close()

# Función adicional para generar informes de ventas
def generar_informe_ventas(fecha_inicio: date, fecha_fin: date) -> Informe:
    conn = get_mysql_conn()
    if conn is None:
        raise HTTPException(status_code=500, detail="Could not connect to SQLite")

    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM Venta WHERE fecha_venta BETWEEN ? AND ?;", 
            (fecha_inicio, fecha_fin)
        )
        ventas_periodo = cursor.fetchall()
        total_ventas = sum(row["cantidad"] for row in ventas_periodo)
        descripcion = f"Informe de ventas del {fecha_inicio} al {fecha_fin}. Total de ventas: {total_ventas}"
        
        nuevo_informe = Informe(
            ID_informe=len(ventas_periodo) + 1,
            tipo_informe="Ventas",
            descripcion=descripcion,
            fecha_generacion=date.today()
        )
        # Guardar informe en la base de datos
        crear_informe(nuevo_informe)
        return nuevo_informe
    finally:
        conn.close()
