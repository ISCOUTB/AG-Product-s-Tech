import pytest
from fastapi.testclient import TestClient
from main import app  # Reemplaza "main" con el nombre de tu archivo principal donde defines `app`

client = TestClient(app)

endpoint = "/marcas"

def test_obtener_todas_marcas():
    response = client.get("/marcas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Verifica que el resultado sea una lista

def test_crear_marca():
    nueva_marca = {
        "Id_marca": 1,
        "nombre": "Marca Prueba",
        "pais_origen": "España"
    }
    response = client.post("/marcas/", json=nueva_marca)
    assert response.status_code == 200
    assert response.json()["message"] == "Marca registrada exitosamente"

def test_obtener_marca_por_id():
    id_marca = 1  # Asegúrate de que este ID exista en la base de datos para pruebas
    response = client.get(f"/marcas/{id_marca}")
    if response.status_code == 200:
        assert "Id_marca" in response.json()
    elif response.status_code == 404:
        assert response.json()["detail"] == "Marca no encontrada"

def test_actualizar_marca():
    id_marca = 1  # Asegúrate de que este ID exista
    marca_actualizada = {
        "nombre": "Marca Actualizada",
        "pais_origen": "México"
    }
    response = client.put(f"/marcas/{id_marca}", json=marca_actualizada)
    if response.status_code == 200:
        assert response.json()["nombre"] == "Marca Actualizada"
    elif response.status_code == 404:
        assert response.json()["detail"] == "Marca no encontrada"

def test_eliminar_marca():
    id_marca = 1  # ID existente para eliminar
    response = client.delete(f"/marcas/{id_marca}")
    if response.status_code == 200:
        assert response.json()["message"] == "Marca eliminada exitosamente"
    elif response.status_code == 404:
        assert response.json()["detail"] == "Marca no encontrada"