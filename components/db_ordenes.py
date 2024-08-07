import sqlite3
from helpers import run_test
from usuarios_log import db_usuarios
from data_sistema import get_system_info
import platform
import os
import psutil

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

db_usuarios()
print("\n+-------------------- Base de datos CREADA ------------------------+")
get_system_info()
run_test()
