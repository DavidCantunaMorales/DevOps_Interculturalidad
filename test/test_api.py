import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))

import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
# Test desde Quito
def test_cultural_greeting(client):
    response = client.get('/cultural-greeting/quito')
    assert response.status_code == 200
    assert response.get_json()['greeting'] == '¡Hola desde Quito!'
# Creación de Estudiantes 
def test_create_estudiante(client):
    response = client.post('/estudiantes', json={"nombre": "Juan", "edad": 20})
    assert response.status_code == 201
    data = response.get_json()
    assert data['nombre'] == 'Juan'
    assert data['edad'] == 20
# GET Estudiantes
def test_get_estudiantes(client):
    response = client.get('/estudiantes')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_update_estudiante(client):
    # Crear estudiante primero
    post_resp = client.post('/estudiantes', json={"nombre": "Ana", "edad": 22})
    estudiante_id = post_resp.get_json()['id']
    # Actualizar
    put_resp = client.put(f'/estudiantes/{estudiante_id}', json={"nombre": "Ana Maria", "edad": 23})
    assert put_resp.status_code == 200
    assert put_resp.get_json()['nombre'] == 'Ana Maria'
    assert put_resp.get_json()['edad'] == 23

def test_delete_estudiante(client):
    # Crear estudiante primero
    post_resp = client.post('/estudiantes', json={"nombre": "Luis", "edad": 25})
    estudiante_id = post_resp.get_json()['id']
    # Eliminar
    del_resp = client.delete(f'/estudiantes/{estudiante_id}')
    assert del_resp.status_code == 200
    assert del_resp.get_json()['message'] == 'Estudiante eliminado'