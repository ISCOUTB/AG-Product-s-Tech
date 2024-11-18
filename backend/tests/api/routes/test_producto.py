import pytest
from fastapi.testclient import TestClient
from main import app  # Reemplaza "main" con el nombre de tu archivo principal donde defines `app`

client = TestClient(app)

# Mock de datos para pruebas
mock_marca = {
    "Id_marca": 1,
    "nombre": "Marca Mock",
    "pais_origen": "México"
}

endpoint = "/productos"

def test_obtener_todos_productos():
    response = client.get("/productos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_crear_producto():
    nuevo_producto = {
        "Id_producto": 1,
        "Nombre": "Producto Test",
        "Categoria": "Tecnología",
        "Descripcion": "Descripción del producto",
        "Precio": 99.99,
        "fecha_lanzamineto": "2023-11-01",
        "Especificaciones": "Especificaciones aquí",
        "Id_Marca": 1
    }
    response = client.post("/productos/", json=nuevo_producto)
    assert response.status_code == 200
    assert response.json()["message"] == "Producto registrado exitosamente"

def test_obtener_producto_por_id():
    producto_id = 1  # ID válido
    response = client.get(f"/productos/{producto_id}")
    if response.status_code == 200:
        assert "Id_producto" in response.json()
    elif response.status_code == 404:
        assert response.json()["detail"] == "Producto no encontrado"

def test_actualizar_producto():
    producto_id = 1  # ID válido
    producto_actualizado = {
        "Id_producto": 1,
        "Nombre": "Producto Test2",
        "Categoria": "Tecnología2",
        "Descripcion": "Descripción actualizada",
        "Precio": 99.98,
        "fecha_lanzamineto": "2023-11-02",
        "Especificaciones": "Especificaciones aquí2",
        "Id_Marca": 2
    }
    response = client.put(f"/productos/{producto_id}", json=producto_actualizado)
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert response.json()["Descripcion"] == "Descripción actualizada"

def test_eliminar_producto():
    producto_id = 1  # ID válido
    response = client.delete(f"/productos/{producto_id}")
    if response.status_code == 200:
        assert response.json()["message"] == "Producto eliminado exitosamente"
    elif response.status_code == 404:
        assert response.json()["detail"] == "Producto no encontrado"