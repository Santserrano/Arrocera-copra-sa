import sqlite3

def crear_base_de_datos():
    # Conectar a la base de datos (se creará si no existe)
    conn = sqlite3.connect('usuarios.db')

    # Crear un cursor
    c = conn.cursor()

    # Crear una tabla
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)''')

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()
