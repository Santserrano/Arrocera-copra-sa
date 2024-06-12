import sqlite3

conn = sqlite3.connect('ordenes.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS ordenes (
                nro TEXT PRIMARY KEY,
                item TEXT NOT NULL,
                cliente TEXT NOT NULL,
                direccion TEXT NOT NULL,
                estado TEXT NOT NULL,
                cantidad TEXT NOT NULL)''')

conn.commit()
conn.close()
