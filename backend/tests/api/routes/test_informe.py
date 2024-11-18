import pytest
from fastapi.testclient import TestClient
from main import app  # Reemplaza "main" con el nombre de tu archivo principal donde defines `app`

client = TestClient(app)

endpoint = "/informes"

def test_obtener_todos_informes():
    response = client.get("/informes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_crear_informe():
    nuevo_informe = {
        "Id_informe": 1,
        "Titulo": "Prueba Informe",
        "Contenido": "Este es un informe de prueba.",
        "Fecha": "2024-11-17"
    }
    response = client.post("/informes/", json=nuevo_informe)
    assert response.status_code == 200
    assert response.json()["message"] == "Informe registrado exitosamente"

def test_obtener_informe_por_id():
    informe_id = 1  # Asegúrate de que este ID exista
    response = client.get(f"/informes/{informe_id}")
    if response.status_code == 200:
        assert "Id_informe" in response.json()
    elif response.status_code == 404:
        assert response.json()["detail"] == "Informe no encontrado"

def test_actualizar_informe():
    informe_id = 1  # Asegúrate de que este ID exista
    informe_actualizado = {
        "Titulo": "Informe Actualizado",
        "Contenido": "Contenido actualizado.",
        "Fecha": "2024-11-18"
    }
    response = client.put(f"/informes/{informe_id}", json=informe_actualizado)
    if response.status_code == 200:
        assert response.json()["Titulo"] == "Informe Actualizado"
    elif response.status_code == 404:
        assert response.json()["detail"] == "Informe no encontrado"

def test_eliminar_informe():
    informe_id = 1  # ID existente para eliminar
    response = client.delete(f"/informes/{informe_id}")
    if response.status_code == 200:
        assert response.json()["message"] == "Informe eliminado exitosamente"
    elif response.status_code == 404:
        assert response.json()["detail"] == "Informe no encontrado"