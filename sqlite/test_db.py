import tkinter as tk
from tkinter import messagebox
import sqlite3

# Función para insertar datos en la base de datos
def insertar_usuario(nombre, edad):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre, edad))
    conn.commit()
    conn.close()
    messagebox.showinfo("Éxito", "Usuario agregado exitosamente")
    entrada_nombre.delete(0, tk.END)
    entrada_edad.delete(0, tk.END)
    mostrar_usuarios()

# Función para mostrar los datos de la base de datos
def mostrar_usuarios():
    lista_usuarios.delete(0, tk.END)
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios")
    filas = c.fetchall()
    for fila in filas:
        lista_usuarios.insert(tk.END, f"ID: {fila[0]}, Usuario: {fila[1]}, Password: {fila[2]}")
    conn.close()


conn = sqlite3.connect('usuarios.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)''')
conn.commit()
conn.close()

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Usuarios")

# Crear widgets
tk.Label(root, text="Usuario").grid(row=0, column=0)
tk.Label(root, text="Contraseña").grid(row=1, column=0)

entrada_nombre = tk.Entry(root)
entrada_nombre.grid(row=0, column=1)

entrada_edad = tk.Entry(root)
entrada_edad.grid(row=1, column=1)

tk.Button(root, text="Agregar Usuario", command=lambda: insertar_usuario(entrada_nombre.get(), entrada_edad.get())).grid(row=2, column=0, columnspan=2)

tk.Button(root, text="Mostrar Usuarios", command=mostrar_usuarios).grid(row=3, column=0, columnspan=2)

lista_usuarios = tk.Listbox(root)
lista_usuarios.grid(row=4, column=0, columnspan=2)

# Ejecutar la aplicación
root.mainloop()
