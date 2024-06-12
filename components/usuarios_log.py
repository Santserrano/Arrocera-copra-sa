import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('usuarios.db')
c = conn.cursor()

# Crear la tabla usuarios si no existe
c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                usuario TEXT PRIMARY KEY,
                password TEXT NOT NULL,
                rol TEXT NOT NULL)''')

# Lista de usuarios con roles
usuarios = [
    ('gerente_general', '1234', 'Gerente_general'),
    ('gerente_transporte', '1234', 'Gerente_transporte'),
    ('gerente_produccion', '1234', 'Gerente_producción')
]

# Insertar los usuarios en la tabla
c.executemany('INSERT OR IGNORE INTO usuarios (usuario, password, rol) VALUES (?, ?, ?)', usuarios)

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()
