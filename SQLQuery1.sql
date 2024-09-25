CREATE TABLE marcas( Id_marca INTEGER PRIMARY KEY NOT NULL, nombre TEXT NOT NULL, pais_origen TEXT NOT NULL) 
CREATE TABLE Producto(Id_producto INTEGER PRIMARY KEY NOT NULL,Nombre TEXT NOT NULL, Categoria TEXT NOT NULL,Descripcion TEXT NOT NULL, Precio FLOAT NOT NULL,fecha_lanzamineto DATE NOT NULL,
Especificaciones TEXT NOT NULL, Id_Marca INTEGER NOT NULL, FOREIGN KEY(Id_marca) REFERENCES marcas(Id_marca))
CREATE TABLE categoria( Id_categoria INTEGER PRIMARY KEY NOT NULL, nombre TEXT NOT NULL, descripcion TEXT NOT NULL)
CREATE TABLE inventario ( Id_inventario INTEGER PRIMARY KEY NOT NULL,Id_producto INTEGER NOT NULL,FOREIGN KEY(Id_PRODUCTO) REFERENCES Producto(Id_producto), cantidad_stock INTEGER NOT NULL , Ubicacion_producto TEXT NOT NULL);
CREATE TABLE proveedor (Id_proveedor INTEGER PRIMARY KEY NOT NULL, nombre TEXT NOT NULL, contacto INTEGER NOT NULL, Direccion TEXT NOT NULL);
CREATE TABLE Clientes (Id_cliente INTEGER PRIMARY KEY NOT NULL,nombre TEXT NOT NULL, email TEXT  NOT NULL, Telefono INTEGER NOT NULL, direccion TEXT NOT NULL);
CREATE TABLE pedido (Id_pedido INTEGER PRIMARY KEY NOT NULL, fecha_pedido DATE NOT NULL, fecha_entrega DATE NOT NULL, Id_cliente INTEGER NOT  NULL,FOREIGN KEY(Id_cliente) REFERENCES Clientes(Id_cliente), estado_pedido TEXT NOT NULL);