Tarea 1 — CRUD en PostgreSQL con Python
Desarrollar una aplicación de consola en Python que gestione una base de datos PostgreSQL sin usar ningún framework ORM (solo la librería psycopg2).

Requerimientos técnicos
1. Base de datos: Crear una base de datos llamada tarea1 en PostgreSQL.

2. Tabla alumno con los siguientes campos:

id — SERIAL PRIMARY KEY
carnet — VARCHAR(15) UNIQUE NOT NULL
nombre — VARCHAR(100) NOT NULL
apellido — VARCHAR(100) NOT NULL
carrera — VARCHAR(150)
email — VARCHAR(150)
telefono — VARCHAR(20)
fecha_registro — DATE DEFAULT CURRENT_DATE
3. Operaciones requeridas (menú interactivo en consola):

Agregar alumno
Modificar datos de un alumno (buscar por carnet)
Listar todos los alumnos
Eliminar alumno (por carnet)
Salir
4. Restricciones:

Solo usar Python puro + psycopg2
No usar SQLAlchemy, Django ORM, ni ningún otro ORM/framework
El script debe crear la tabla automáticamente si no existe al iniciar