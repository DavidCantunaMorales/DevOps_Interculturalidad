import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, jsonify, request
from app.database import init_db, create_estudiante, get_all_estudiantes, get_estudiante, update_estudiante, delete_estudiante

app = Flask(__name__)

# Inicializar la base de datos
init_db()

# Endpoint cultural-greeting (requerido por el taller)
@app.route('/cultural-greeting/<country>')
def cultural_greeting(country):
    greetings = {
        'quito': '¡Hola desde Quito - Ecuador!',
        'espana': '¡Hola desde Barcelona - España!',
        'china': 'Ni hao, Sage!',
        'cuenca': '¡Saludos desde Cuenca - Ecuador!',
    }
    greeting = greetings.get(country.lower(), 'Hello!')
    return jsonify({"country": country, "greeting": greeting})

# CRUD Endpoints
@app.route('/estudiantes', methods=['POST'])
def create_estudiante_endpoint():
    data = request.get_json()
    if not data or 'nombre' not in data or 'edad' not in data:
        return jsonify({"error": "Faltan nombre o edad"}), 400
    id = create_estudiante(data['nombre'], data['edad'])
    if id:
        return jsonify({"id": id, "nombre": data['nombre'], "edad": data['edad']}), 201
    return jsonify({"error": "No se pudo crear el estudiante"}), 500

@app.route('/estudiantes', methods=['GET'])
def get_estudiantes_endpoint():
    estudiantes = get_all_estudiantes()
    return jsonify(estudiantes)

@app.route('/estudiantes/<int:id>', methods=['GET'])
def get_estudiante_endpoint(id):
    estudiante = get_estudiante(id)
    if not estudiante:
        return jsonify({"error": "Estudiante no encontrado"}), 404
    return jsonify(estudiante)

@app.route('/estudiantes/<int:id>', methods=['PUT'])
def update_estudiante_endpoint(id):
    data = request.get_json()
    if not data or 'nombre' not in data or 'edad' not in data:
        return jsonify({"error": "Faltan nombre o edad"}), 400
    if update_estudiante(id, data['nombre'], data['edad']):
        return jsonify({"id": id, "nombre": data['nombre'], "edad": data['edad']})
    return jsonify({"error": "Estudiante no encontrado"}), 404

@app.route('/estudiantes/<int:id>', methods=['DELETE'])
def delete_estudiante_endpoint(id):
    if delete_estudiante(id):
        return jsonify({"message": "Estudiante eliminado"})
    return jsonify({"error": "Estudiante no encontrado"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)