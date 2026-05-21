import psycopg2

DB_config={
    "host": "localhost",
    "database":"tarea1",
    "user":"postgres",
    "password":"orellana5108p",
}

def conexion():
    try:
        return psycopg2.connect(**DB_config)
    except Exception as e:
        print(f"Error de conexion: {e}")
        return None

def inicializar_base():
    query = """
    CREATE TABLE IF NOT EXISTS alumno (
        id SERIAL PRIMARY KEY,
        carnet VARCHAR(15) UNIQUE NOT NULL,
        nombre VARCHAR(100) NOT NULL,
        apellido VARCHAR(100) NOT NULL,
        carrera VARCHAR(150),
        email VARCHAR(150),
        telefono VARCHAR(20),
        fecha_registro DATE DEFAULT CURRENT_DATE
    );
    """
    conn = conexion()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
        conn.close()
        print("Conexión exitosa la tabla 'alumno' está lista")


def agregar_alumno():
    print("\n--- AGREGAR ALUMNO ---")
    carnet = input("carnet: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    carrera = input("Carrera: ")
    email = input("Email: ")
    telefono = input("Teléfono: ")

    query = """
    INSERT INTO alumno(carnet,nombre,apellido, carrera, email,telefono)
    values(%s,%s,%s,%s,%s,%s)
    """

    conn= conexion()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, (carnet, nombre, apellido, carrera, email, telefono))
                conn.commit()
            print(f"¡Alumno {nombre} {apellido} agregado con éxito!")
        except Exception as e:
            print(f"Error al agregar alumno: {e}")
        finally:
            conn.close()

def listar_alumnos():
    print("\n--- LISTA DE ALUMNOS ---")
    query = "SELECT carnet, nombre, apellido, carrera, email, telefono FROM alumno;"
    
    conn = conexion()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute(query)
                alumnos = cursor.fetchall()
                
                if not alumnos:
                    print("No hay alumnos registrados.")
                else:
                    for al in alumnos:
                        print(f"Carnet: {al[0]} | Nombre: {al[1]} {al[2]} | Carrera: {al[3]} | Email: {al[4]} | Tel: {al[5]}")
        except Exception as e:
            print(f"error al listar alumnos: {e}")
        finally:
            conn.close()

def modificar_alumno():
    print("\n--- MODIFICAR ALUMNO ---")
    carnet = input("Ingrese el carnet del alumno a modificar: ")
    
    nombre = input("Nuevo Nombre: ")
    apellido = input("Nuevo Apellido: ")
    carrera = input("Nueva Carrera: ")
    email = input("Nuevo Email: ")
    telefono = input("Nuevo Teléfono: ")

    query = """
    UPDATE alumno 
    SET nombre = %s, apellido = %s, carrera = %s, email = %s, telefono = %s
    WHERE carnet = %s
    """
    
    conn = conexion()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, (nombre, apellido, carrera, email, telefono, carnet))
                
                if cursor.rowcount == 0:
                    print("No se encontró ningún alumno con ese carnet.")
                else:
                    conn.commit() # Guardamos los cambios
                    print("¡Datos actualizados con éxito!")
        except Exception as e:
            print(f"Error al modificar: {e}")
        finally:
            conn.close()

def eliminar_alumno():
    print("\n--- ELIMINAR ALUMNO ---")
    carnet = input("Ingrese el carnet del alumno a eliminar: ")
    
    query = "DELETE FROM alumno WHERE carnet = %s"
    
    conn = conexion()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, (carnet,))
                
                if cursor.rowcount == 0:
                    print("No se encontró ningún alumno con ese carnet.")
                else:
                    conn.commit() 
                    print("¡Alumno eliminado con éxito!")
        except Exception as e:
            print(f"Error al eliminar: {e}")
        finally:
            conn.close()

def mostrar_menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Agregar alumno")
        print("2. Modificar datos de un alumno")
        print("3. Listar todos los alumnos")
        print("4. Eliminar alumno")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == '1':
            agregar_alumno()
        elif opcion == '2':
            modificar_alumno()
        elif opcion == '3':
            listar_alumnos()
        elif opcion == '4':
            eliminar_alumno()
        elif opcion == '5':
            print("Cerrando la aplicación")
            break
        else:
            print("Opción no válida. Por favor intente de nuevo")

if __name__ == "__main__":
    inicializar_base()
    mostrar_menu()