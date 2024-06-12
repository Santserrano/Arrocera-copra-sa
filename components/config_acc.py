import tkinter
import tkintermapview
from customtkinter import *
from PIL import Image, ImageTk
import os
import sqlite3
#------------------------------------------------------------------------------------------------------>

def modificar_usuario(usuario, nueva_password):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()

    c.execute('''UPDATE usuarios 
                 SET password = ? 
                 WHERE usuario = ?''', (nueva_password, usuario))
    
    conn.commit()
    conn.close()

def verificar_cuenta(usuario, actual_password, nueva_password):

    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()

    c.execute('''SELECT * FROM usuarios 
                 WHERE usuario = ? AND password = ?''', (usuario, actual_password))
    resultado = c.fetchone()

    if resultado: # Si es verdadero modifica en la db
        modificar_usuario(usuario, nueva_password)

    conn.close()

# Ventana
def config_acc():

    def volver(root):
        from dashboard import dashboard
        root.destroy()
        dashboard()

    app = CTk()
    app.geometry(f"{856}x{645}")
    app.resizable(0,0)
    app.title("Configuración de cuenta - Copra S.A")
    logo_img_data = Image.open("assets/logo.png")

    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    window_width = 856
    window_height = 645
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2 - 50
    # Centro del escritorio
    app.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    # Fondo azul marino
    master_app = CTkFrame(master=app, fg_color="#003b48", width=856, height=645)
    master_app.pack_propagate(0)
    master_app.pack(expand=True)

    # Instancia de logo
    logo_img = CTkImage(logo_img_data, size=(50, 55))

    # Barra superior menú
    title_frame = CTkFrame(master=master_app, fg_color="#d9ecec", corner_radius=0)
    title_frame.pack(fill="x", pady=(0, 20), ipady=3)

    # Configuración de las columnas del grid
    title_frame.columnconfigure(0, weight=1)
    title_frame.columnconfigure(1, weight=1)
    title_frame.columnconfigure(2, weight=1)

    CTkLabel(master=title_frame, text="", image=logo_img).grid(row=0, column=0, padx=(10, 0), pady=(3, 0), sticky="w")
    CTkLabel(master=title_frame, text="CONFIGURACIÓN DE CUENTA", font=("Poppins Bold", 25), text_color="#003b48").grid(row=0, column=1, pady=(12, 0), sticky="n")
    CTkButton(master=title_frame, width=100, height=30, command=lambda: volver(app), text="<  Volver", font=("Poppins Bold", 15), text_color="#fff", fg_color="#003b48", hover_color="#006278").grid(row=0, column=2, padx=(0, 10), sticky="e")

    #------------------------------------------------------------------------------------------------------>
    grid = CTkFrame(master=master_app, fg_color="transparent")
    grid.pack(fill="both", padx=(210, 0), pady=(100,0))

    CTkLabel(master=grid, text="Nombre de usuario actual", font=("Poppins Bold", 15), text_color="#fff").grid(row=0, column=1, sticky="w")
    usuario = CTkEntry(master=grid, fg_color="#d5eae8", border_width=0, width=400, text_color="#003b48")
    usuario.grid(row=1, column=1, ipady=10, pady=(0, 10))

    CTkLabel(master=grid, text="Contraseña actual", font=("Poppins Bold", 15), text_color="#fff").grid(row=2, column=1, sticky="w")
    actual_password = CTkEntry(master=grid, fg_color="#d5eae8", border_width=0, width=400, text_color="#003b48")
    actual_password.grid(row=3, column=1, ipady=10, pady=(0, 10))

    CTkLabel(master=grid, text="Nueva contraseña", font=("Poppins Bold", 15), text_color="#fff").grid(row=4, column=1, sticky="w")
    nueva_password = CTkEntry(master=grid, fg_color="#d5eae8", border_width=0, width=400, text_color="#003b48")
    nueva_password.grid(row=5, column=1, ipady=10, pady=(0, 40))

    CTkButton(master=grid, text="Guardar cambios", width=300, command=lambda: verificar_cuenta(usuario.get(), actual_password.get(), nueva_password.get()), font=("Poppins Bold", 15), border_width=3, border_color="#fff", hover_color="#006278", fg_color="#003b48", text_color="#fff").grid(row=6, column=1)


    app.mainloop()

if __name__ == "__main__":
    config_acc()