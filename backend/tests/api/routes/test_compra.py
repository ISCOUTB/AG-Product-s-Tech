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

endpoint = "/compras"

def test_obtener_todas_compras():
    response = client.get("/compras/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_crear_compra():
    nueva_compra = {
        "Id_compra": 1,
        "Id_producto": 1,
        "Cantidad": 10,
        "Fecha": "2024-11-17"
    }
    response = client.post("/compras/", json=nueva_compra)
    assert response.status_code == 200
    assert response.json()["message"] == "Compra registrada exitosamente"

def test_obtener_compra_por_id():
    compra_id = 1  # Asegúrate de que este ID exista
    response = client.get(f"/compras/{compra_id}")
    if response.status_code == 200:
        assert "Id_compra" in response.json()
    elif response.status_code == 404:
        assert response.json()["detail"] == "Compra no encontrada"

def test_actualizar_compra():
    compra_id = 1  # Asegúrate de que este ID exista
    compra_actualizada = {
        "Id_producto": 2,
        "Cantidad": 20,
        "Fecha": "2024-11-18"
    }
    response = client.put(f"/compras/{compra_id}", json=compra_actualizada)
    if response.status_code == 200:
        assert response.json()["Cantidad"] == 20
    elif response.status_code == 404:
        assert response.json()["detail"] == "Compra no encontrada"

def test_eliminar_compra():
    compra_id = 1  # ID existente para eliminar
    response = client.delete(f"/compras/{compra_id}")
    if response.status_code == 200:
        assert response.json()["message"] == "Compra eliminada exitosamente"
    elif response.status_code == 404:
        assert response.json()["detail"] == "Compra no encontrada"