from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class Usuario(BaseModel):
    nombre_completo: str
    nick: str
    email: EmailStr
    contrasena: str

class Producto(BaseModel):
    Id_producto: Optional[int]
    Nombre: str
    Categoria: str
    Descripcion: str
    Precio: float
    fecha_lanzamineto: date
    Especificaciones: str
    Id_Marca: int

class Inventario(BaseModel):
    Id_inventario: Optional[int]
    Id_producto: int
    cantidad_stock: int
    Ubicacion_producto: str

class Proveedor(BaseModel):
    Id_proveedor: Optional[int]
    nombre: str
    contacto: int
    Direccion: str

class Cliente(BaseModel):
    Id_cliente: Optional[int]
    nombre: str
    email: EmailStr
    Telefono: int
    direccion: str

class Pedido(BaseModel):
    Id_pedido: Optional[int]
    fecha_pedido: date
    fecha_entrega: date
    Id_cliente: int
    estado_pedido: str

class Venta(BaseModel):
    Id_venta: Optional[int]
    Id_producto: int
    Cantidad: int
    Fecha: date

class Compra(BaseModel):
    Id_compra: Optional[int]
    Id_producto: int
    Cantidad: int
    Fecha: date

class Informe(BaseModel):
    Id_informe: Optional[int]
    Titulo: str
    Contenido: str
    Fecha: date

class Marca(BaseModel):
    Id_marca: Optional[int]
    nombre: str
    pais_origen: str

class Categoria(BaseModel):
    Id_categoria: Optional[int]
    nombre: str
    descripcion: str

class LoginData(BaseModel):
    email: EmailStr
    password: str