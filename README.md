Tarea 1 - CRUD en PostgreSQL con Python

Aplicación de consola en Python para gestionar una base de datos de alumnos en PostgreSQL, desarrollada sin utilizar frameworks ORM (únicamente utilizando la librería `psycopg2`).

Requerimientos Técnicos
- Python 3.x
- PostgreSQL
- Librería `psycopg2-binary`

preparación del Entorno
1. Crear una base de datos en PostgreSQL llamada `tarea1`.
2. Instalar la dependencia necesaria ejecutando en la terminal:
   ```bash
   pip install psycopg2-binary
3. Configurar las credenciales de PostgreSQL (usuario y contraseña) en el diccionario DB_config dentro del archivo main.py.

Ejecución
Para iniciar la aplicación y el menú interactivo, ejecuta el siguiente comando en la terminal:
python main.py