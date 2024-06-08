import sqlite3
"""
Pequeño script para imprimir en consola los
usuarios de la db :p
"""
conn = sqlite3.connect('usuarios.db')

c = conn.cursor()

c.execute("SELECT * FROM usuarios")
filas = c.fetchall() #recupero filas

for fila in filas:
    print(fila)

conn.close()
