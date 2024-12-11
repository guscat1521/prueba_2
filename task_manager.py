import pyodbc
# Configuración de la conexión a SQL Server
connection_string = (
    "Driver={SQL Server};"
    "Server=DESKTOP-XXXXXX;"  # Cambia por el nombre de tu servidor o usa localhost
    "Database=TaskManager;"    # Nombre de la base de datos que creaste
    "Trusted_Connection=yes;"  # O usa un usuario/contraseña si configuraste autenticación SQL
)

try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    print("Conexión exitosa a SQL Server.")
except pyodbc.Error as e:
    print(f"Error al conectar a la base de datos: {e}")

def add_task(title, description, due_date, priority):
    try:
        query = """
        INSERT INTO Tasks (title, description, due_date, priority, completed)
        VALUES (?, ?, ?, ?, 0)
        """
        cursor.execute(query, (title, description, due_date, priority))
        conn.commit()
        print("Tarea agregada correctamente.")
    except pyodbc.Error as e:
        print(f"Error al agregar la tarea: {e}")

def list_tasks():
    try:
        query = "SELECT * FROM Tasks WHERE completed = 0"
        cursor.execute(query)
        tasks = cursor.fetchall()

        if not tasks:
            print("No hay tareas pendientes.")
        else:
            for task in tasks:
            print(f"ID: {task[0]}, Título: {task[1]}, Fecha límite: {task[3]}, Prioridad: {task[4]}")
    except pyodbc.Error as e:
        print(f"Error al listar las tareas: {e}")

def complete_task(task_id):
    try:
        query = "UPDATE Tasks SET completed = 1 WHERE task_id = ?"
        cursor.execute(query, task_id)
        conn.commit()
        print(f"Tarea con ID {task_id} marcada como completada.")
    except pyodbc.Error as e:
        print(f"Error al completar la tarea: {e}")

def delete_task(task_id):
    try:
        query = "DELETE FROM Tasks WHERE task_id = ?"
        cursor.execute(query, task_id)
        conn.commit()
        print(f"Tarea con ID {task_id} eliminada.")
    except pyodbc.Error as e:
        print(f"Error al eliminar la tarea: {e}")
    except Exception as ex:
        print(f"Ocurrió un error: {ex}")


def menu():
    while True:
        print("\n--- Sistema de Gestión de Tareas ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        choice = input("Selecciona una opción: ")

        if choice == '1':
            title = input("Título de la tarea: ")
            description = input("Descripción: ")
            due_date = input("Fecha límite (YYYY-MM-DD): ")
            priority = input("Prioridad (Baja, Media, Alta): ")
            add_task(title, description, due_date, priority)

        elif choice == '2':
            list_tasks()

        elif choice == '3':
            task_id = int(input("ID de la tarea a completar: "))
            complete_task(task_id)

        elif choice == '4':
            task_id = int(input("ID de la tarea a eliminar: "))
            delete_task(task_id)

        elif choice == '5':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    menu()
