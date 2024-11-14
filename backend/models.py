from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    username: str
    email: str
    password: str
    full_name: str

class LoginData(BaseModel):
    email: str
    password: str

class Producto(BaseModel):
    ID_producto: int
    Nombre: str
    Descripcion: str
    categoria: int
    precio: float
    fecha_lanzamiento: date
    ID_marca: int

class Inventario(BaseModel):
    ID_inventario: int
    ID_producto: int
    cantidad_stock: int
    ubicacion_producto: str

class Venta(BaseModel):
    ID_venta: int
    ID_producto: int
    cantidad: int
    fecha_venta: date

class Compra(BaseModel):
    ID_compra: int
    ID_producto: int
    cantidad: int
    proveedor: str
    fecha_compra: date

class Informe(BaseModel):
    ID_informe: int
    tipo_informe: str
    descripcion: str
    fecha_generacion: date
