import pytest
from fastapi.testclient import TestClient
from main import app  # Reemplaza "main" con el nombre de tu archivo principal donde defines `app`

client = TestClient(app)

endpoint = "/usuarios"

def test_obtener_todos_usuarios():
    response = client.get("/usuarios/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_crear_usuario():
    nuevo_usuario = {
        "nombre_completo": "John Doe",
        "nick": "johnd",
        "email": "johndoe@example.com",
        "contrasena": "password123"
    }
    response = client.post("/usuarios/", json=nuevo_usuario)
    assert response.status_code == 200
    assert response.json()["message"] == "Usuario registrado exitosamente"

def test_obtener_usuario_por_id():
    user_id = 1  # Asegúrate de tener un ID válido
    response = client.get(f"/usuarios/{user_id}")
    if response.status_code == 200:
        assert "Id_usuario" in response.json()
    elif response.status_code == 404:
        assert response.json()["detail"] == "Usuario no encontrado"

def test_actualizar_usuario():
    user_id = 1  # ID válido
    usuario_actualizado = {
        "nombre_completo": "John Doe2",
        "nick": "johnd2",
        "email": "johndoe2@example.com",
        "contrasena": "password1232"
    }
    response = client.put(f"/usuarios/{user_id}", json=usuario_actualizado)
    assert response.status_code in [200, 404]  # Puede fallar si no existe
    if response.status_code == 200:
        assert response.json()["nick"] == "johnd2"

def test_eliminar_usuario():
    user_id = 1  # ID válido
    response = client.delete(f"/usuarios/{user_id}")
    if response.status_code == 200:
        assert response.json()["message"] == "Usuario eliminado exitosamente"
    elif response.status_code == 404:
        assert response.json()["detail"] == "Usuario no encontrado"