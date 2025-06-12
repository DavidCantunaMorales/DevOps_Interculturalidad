#!/bin/sh

echo "🔄 Esperando a que MySQL esté disponible en $DB_HOST:3306..."

# Esperar hasta que el puerto 3306 del contenedor `db` esté abierto
while ! nc -z $DB_HOST 3306; do
  sleep 1
done

echo "✅ MySQL está listo. Iniciando aplicación..."

# Ejecutar la app con inicialización incluida
python app/main.py
