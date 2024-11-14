CREATE TABLE users (
    Id_usuario INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nombre_completo VARCHAR(255) NOT NULL,
    nick VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL
);

CREATE TABLE marcas (
    Id_marca INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    pais_origen VARCHAR(255) NOT NULL
);

CREATE TABLE Producto (
    Id_producto INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    Nombre VARCHAR(255) NOT NULL,
    Categoria VARCHAR(255) NOT NULL,
    Descripcion TEXT NOT NULL,
    Precio FLOAT NOT NULL,
    fecha_lanzamineto DATE NOT NULL,
    Especificaciones TEXT NOT NULL,
    Id_Marca INT NOT NULL,
    FOREIGN KEY (Id_Marca) REFERENCES marcas(Id_marca)
);

CREATE TABLE categoria (
    Id_categoria INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT NOT NULL
);

CREATE TABLE inventario (
    Id_inventario INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    Id_producto INT NOT NULL,
    FOREIGN KEY (Id_producto) REFERENCES Producto(Id_producto),
    cantidad_stock INT NOT NULL,
    Ubicacion_producto VARCHAR(255) NOT NULL
);

CREATE TABLE proveedor (
    Id_proveedor INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    contacto BIGINT NOT NULL,
    Direccion TEXT NOT NULL
);

CREATE TABLE Clientes (
    Id_cliente INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    Telefono BIGINT NOT NULL,
    direccion TEXT NOT NULL
);

CREATE TABLE pedido (
    Id_pedido INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    fecha_pedido DATE NOT NULL,
    fecha_entrega DATE NOT NULL,
    Id_cliente INT NOT NULL,
    FOREIGN KEY (Id_cliente) REFERENCES Clientes(Id_cliente),
    estado_pedido VARCHAR(255) NOT NULL
);
