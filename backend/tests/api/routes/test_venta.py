import pytest
from fastapi.testclient import TestClient
from main import app  # Reemplaza "main" con el nombre de tu archivo principal donde defines `app`

client = TestClient(app)

# Mock de datos para pruebas
mock_producto = {
    "Id_producto": 1,
    "Nombre": "Producto Test",
    "Categoria": "Tecnología",
    "Descripcion": "Descripción del producto",
    "Precio": 99.99,
    "fecha_lanzamineto": "2023-11-01",
    "Especificaciones": "Especificaciones aquí",
    "Id_Marca": 1
}

endpoint = "/ventas"

def test_obtener_todas_ventas():
    response = client.get("/ventas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Verifica que sea una lista

def test_crear_venta():
    nueva_venta = {
        "Id_venta": 1,
        "Id_producto": 1,
        "Cantidad": 5,
        "Fecha": "2024-11-17"
    }
    response = client.post("/ventas/", json=nueva_venta)
    assert response.status_code == 200
    assert response.json()["message"] == "Venta registrada exitosamente"

def test_obtener_venta_por_id():
    venta_id = 1  # Asegúrate de que este ID exista en tu base de datos para pruebas
    response = client.get(f"/ventas/{venta_id}")
    if response.status_code == 200:
        assert "Id_venta" in response.json()
    elif response.status_code == 404:
        assert response.json()["detail"] == "Venta no encontrada"

def test_actualizar_venta():
    venta_id = 1  # Asegúrate de que este ID exista
    venta_actualizada = {
        "Id_producto": 2,
        "Cantidad": 10,
        "Fecha": "2024-11-18"
    }
    response = client.put(f"/ventas/{venta_id}", json=venta_actualizada)
    if response.status_code == 200:
        assert response.json()["Id_producto"] == 2
    elif response.status_code == 404:
        assert response.json()["detail"] == "Venta no encontrada"

def test_eliminar_venta():
    venta_id = 1  # ID existente para eliminar
    response = client.delete(f"/ventas/{venta_id}")
    if response.status_code == 200:
        assert response.json()["message"] == "Venta eliminada exitosamente"
    elif response.status_code == 404:
        assert response.json()["detail"] == "Venta no encontrada"