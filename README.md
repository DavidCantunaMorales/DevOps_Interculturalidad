# DevOps_Interculturalidad


| Persona            | Rol                 | Tareas                                                                 | Herramientas                     |
|--------------------|---------------------|-----------------------------------------------------------------------|----------------------------------|
| **David Cantuña**  | Desarrollador       | - Implementar endpoints: `POST /estudiantes` (crear estudiante) y `GET /estudiantes` (listar estudiantes).<br>- Gestionar el código en un repositorio Git (crear rama `feature/crud-david`). | Python (Flask/FastAPI) o Node.js (Express), Git |
| **Sebastián Torres**| Desarrollador       | - Implementar endpoints: `GET /estudiantes/:id` (obtener estudiante por ID), `PUT /estudiantes/:id` (actualizar estudiante), y `DELETE /estudiantes/:id` (eliminar estudiante).<br>- Gestionar el código en Git (crear rama `feature/crud-sebastian`). | Python (Flask/FastAPI) o Node.js (Express), Git |
| **Mateo Román**    | Tester              | - Crear pruebas automatizadas para todos los endpoints del CRUD usando pytest (Python) o Jest (Node.js).<br>- Configurar GitHub Actions para ejecutar pruebas automáticamente al hacer push. | pytest/Jest, GitHub Actions      |
| **Luis Burbano**   | Ingeniero DevOps    | - Crear un `Dockerfile` para la aplicación (usando Python/Node.js y SQLite).<br>- Configurar GitHub Actions para automatizar el build y push del contenedor a un registro (ej. Docker Hub). | Docker, GitHub Actions           |


# Análisis de Colaboración

## Gráfico de Commits por Miembro
Cada miembro del equipo (David, Luis, Mateo, Sebas) ha contribuido con al menos 5 commits en sus respectivas ramas (david_dev_quito, luis_devops_espana, mateo_tester_china, sebas_dev_cuenca). El gráfico fue generado utilizando un script de Python (generate_commit_graph.py) y refleja una distribución equitativa de commits, cumpliendo con los requisitos de la rúbrica.

## Tiempo Promedio para Resolver PRs
El tiempo promedio para resolver los pull requests (PRs) fue de 38 horas, calculado manualmente a partir de los PRs cerrados en el repositorio. Este valor representa el tiempo transcurrido desde la creación hasta el merge o cierre de cada PR. Para mejorar la eficiencia, recomendamos establecer un SLA (Service Level Agreement) de 24 horas para revisiones de PRs en futuros proyectos.

## Reflexiones

### ¿Cómo se resolvieron los conflictos de timezone?
Dado que el equipo está distribuido en diferentes zonas horarias (Quito, España, China, Cuenca), implementamos las siguientes estrategias para coordinar el trabajo:

- **Comunicación asíncrona**: Utilizamos GitHub Discussions para acordar horarios de merge, definiendo ventanas de tiempo comunes (por ejemplo, 10:00-12:00 UTC).
- **Notificaciones automáticas**: Configuramos GitHub Actions para enviar alertas a través de Slack o correo electrónico cuando se creaba o revisaba un PR, permitiendo una respuesta rápida a pesar de las diferencias horarias.
- **Ventana de colaboración**: Identificamos un período de 2 horas diarias (08:00-10:00 UTC) donde todos los miembros podían estar disponibles para discusiones urgentes o revisiones críticas.

### ¿Qué pasaría si el equipo en India no tiene acceso a Docker Hub?
Si el equipo en India no tuviera acceso a Docker Hub, se presentarían los siguientes problemas y soluciones:

- **Impacto**: La imposibilidad de descargar imágenes base (como python:3.9 o node:16) o de publicar imágenes generadas interrumpiría el flujo de CI/CD configurado en GitHub Actions.
- **Soluciones**:
  - **Registro local**: Configurar un registro de contenedores local, como Harbor o Nexus, para almacenar imágenes y reducir la dependencia de Docker Hub.
  - **Imágenes pre-descargadas**: Proveer imágenes base pre-descargadas en un almacenamiento interno accesible para el equipo en India.
  - **Registros alternativos**: Utilizar registros públicos como GitHub Container Registry (ghcr.io) o Amazon ECR, si están disponibles en la región.
  - **Construcción offline**: Modificar el Dockerfile para usar paquetes locales o cachés, aunque esto podría limitar la portabilidad.

**Recomendación**: Incluir un plan de contingencia en el README del proyecto, con instrucciones claras para configurar un registro alternativo en caso de restricciones de acceso.

## Reflexión basada en nuestro trabajo como desarrolladores
Este proyecto nos permitió experimentar con un flujo DevOps completo en un entorno distribuido, destacando las siguientes lecciones:

- **Convenciones claras**: Las ramas nombradas por región (david_dev_quito, sebas_dev_cuenca, etc.) facilitaron el seguimiento del trabajo, pero requirieron una convención estricta para evitar conflictos.
- **Automatización eficiente**: La configuración de GitHub Actions para pruebas automáticas y builds de Docker redujo errores manuales, aunque demandó tiempo inicial para su correcta implementación.
- **Colaboración intercultural**: Adaptarnos a diferentes zonas horarias y estilos de trabajo nos enseñó a ser más empáticos y precisos en la comunicación. Por ejemplo, los comentarios en los PRs debían ser detallados para evitar malentendidos entre regiones.

## Propuestas de mejora
- Implementar asignaciones automáticas de revisores en GitHub Actions para agilizar las revisiones de PRs.
- Usar un tablero Kanban en GitHub Projects para visualizar el progreso del equipo y mejorar la coordinación.
- Documentar mejor las dependencias del proyecto (como acceso a Docker Hub) para anticipar problemas en entornos restringidos.

