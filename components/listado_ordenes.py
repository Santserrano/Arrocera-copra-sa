from customtkinter import *
from PIL import Image, ImageTk
import os
from CTkTable import CTkTable
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter
import os
import sqlite3

#------------------------------------------------------------------------------------------------------>
"""
Instancia de ventana,
color de fondo y logo.
"""

# Ventana
def listado_ordenes():

    def volver(root):
        root.destroy()
        from dashboard import dashboard
        dashboard()

    app = CTk()
    app.geometry(f"{856}x{645}")
    app.resizable(0,0)
    app.title("Listado Ordenes - Copra S.A")
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
    title_frame.pack(fill="x", pady=(0, 0), ipady=3)

    # Configuración de las columnas del grid
    title_frame.columnconfigure(0, weight=1)
    title_frame.columnconfigure(1, weight=1)
    title_frame.columnconfigure(2, weight=1)

    CTkLabel(master=title_frame, text="", image=logo_img).grid(row=0, column=0, padx=(10, 0), pady=(3, 0), sticky="w")
    CTkLabel(master=title_frame, text="LISTADO ORDENES", font=("Poppins Bold", 25), text_color="#003b48").grid(row=0, column=1, pady=(12, 0), sticky="n")
    CTkButton(master=title_frame, width=100, height=30, command=lambda: volver(app), text="<  Volver", font=("Poppins Bold", 15), text_color="#fff", fg_color="#003b48", hover_color="#006278").grid(row=0, column=2, padx=(0, 10), sticky="e")

    #------------------------------------------------------------------------------------------------------>

    table_data = [
        ["N° Orden", "Item", "Cliente", "Dirección", "Estado", "Cantidad"],
        ['3833', 'Arroz blanco', 'Juan Perez', 'Av. Rivadavia 123', 'Enviado', '8'],
        ['6432', 'Arroz integral', 'María Gomez', 'Calle Corrientes 456', 'Entregado', '10'],
        ['2180', 'Arroz blanco', 'Pedro Rodriguez', 'Av. Belgrano', 'Pendiente', '3'],
        ['5412', 'Arroz basmati', 'Ana Fernandez', 'Calle San Martin 789', 'Enviado', '5'],
        ['6587', 'Arroz jazmín', 'Luis Martinez', 'Av. Santa Fe 321', 'Pendiente', '2'],
        ['7432', 'Arroz integral', 'Sofia Lopez', 'Calle Mitre 654', 'Entregado', '7'],
        ['8743', 'Arroz blanco', 'Carlos Gomez', 'Av. Callao 987', 'Enviado', '6'],
        ['9123', 'Arroz basmati', 'Elena Garcia', 'Calle Lavalle 123', 'Pendiente', '4']
    ]

    table_frame = CTkScrollableFrame(master=master_app, fg_color="transparent")
    table_frame.pack(expand=True, fill="both", padx=27, pady=0)
    table = CTkTable(master=table_frame, values=table_data, colors=["#E6E6E6", "#EEEEEE"], text_color="#003b48", header_color="#003b48", hover_color="#d5eae8")
    table.edit_row(0, text_color="#fff", hover_color="#006278")
    table.pack(expand=True)

    conn = sqlite3.connect('ordenes.db')
    c = conn.cursor()

    ################################## Query a la db
    c.execute("SELECT * FROM ordenes")
    ordenes = c.fetchall()
    conn.close()
    #table.clear()

    for orden in ordenes:
        table.add_row(orden)
    
    frame_inferior = CTkFrame(master=master_app, fg_color="#0299ba", width=856, height=400)
    frame_inferior.pack(expand=True, pady=(0, 60), side="top")

    # Configuración de las columnas del grid
    frame_inferior.columnconfigure(0, weight=1)
    frame_inferior.columnconfigure(1, weight=1)
    frame_inferior.columnconfigure(2, weight=1)

    #------------------------------------------------------------------------------------------------------#
    tarjeta_1 = CTkFrame(master=frame_inferior, width=240, height=150, fg_color="#fff", border_color="#003b48", border_width=3)
    tarjeta_1.grid_propagate(0)
    tarjeta_1.grid(row=0, column=0, padx=(10, 5), pady=(10, 10))
    # Contenido de la tarjeta
    # Título
    silo_label = CTkLabel(master=tarjeta_1, text="Arroz basmati", font=("Poppins Medium", 18), text_color="#171717")
    silo_label.grid(row=0, column=0, padx=(20, 0), pady=(15, 5), sticky="w")
    # Icono
    icon_img = Image.open("assets/icon-arroz.png").resize((20, 20))
    icon_photo = CTkImage(icon_img)
    icon_label = CTkLabel(master=tarjeta_1, image=icon_photo, text="")
    icon_label.grid(row=0, column=0, padx=(180, 0), pady=(10, 5), sticky="w")
    #------------------>
    # Información del silo 1
    # Toneladas
    toneladas_label = CTkLabel(master=tarjeta_1, text="Silo 4", font=("Poppins Light", 13), text_color="#171717")
    toneladas_label.grid(row=1, column=0, padx=(20, 0), pady=(0, 0), sticky="w")
    toneladas_valor = CTkLabel(master=tarjeta_1, text="Disponibilidad: 5 toneladas", font=("Poppins Bold", 14), text_color="#ff3b3b")
    toneladas_valor.grid(row=2, column=0, padx=(20, 0), pady=(0, 0), sticky="w")

    #------------------------------------------------------------------------------------------------------#
    tarjeta_2 = CTkFrame(master=frame_inferior, width=240, height=150, fg_color="#fff", border_color="#003b48", border_width=3)
    tarjeta_2.grid_propagate(0)
    tarjeta_2.grid(row=0, column=1, padx=(5, 5), pady=(10, 10))
    # Contenido de la tarjeta
    # Título
    silo_label2 = CTkLabel(master=tarjeta_2, text="Arroz integral", font=("Poppins Medium", 18), text_color="#171717")
    silo_label2.grid(row=0, column=0, padx=(20, 0), pady=(15, 5), sticky="w")
    # Icono
    icon_img = Image.open("assets/icon-arroz.png").resize((20, 20))
    icon_photo = CTkImage(icon_img)
    icon_label = CTkLabel(master=tarjeta_2, image=icon_photo, text="")
    icon_label.grid(row=0, column=0, padx=(180, 0), pady=(10, 5), sticky="w")
    #------------------>
    # Información del silo 2
    # Toneladas
    toneladas_label2 = CTkLabel(master=tarjeta_2, text="Silo 1", font=("Poppins Light", 13), text_color="#171717")
    toneladas_label2.grid(row=1, column=0, padx=(20, 0), pady=(0, 0), sticky="w")
    toneladas_valor2 = CTkLabel(master=tarjeta_2, text="Disponibilidad: 6 toneladas", font=("Poppins Bold", 14), text_color="#ff3b3b")
    toneladas_valor2.grid(row=2, column=0, padx=(20, 0), pady=(0, 0), sticky="w")

    #------------------------------------------------------------------------------------------------------#
    tarjeta_3 = CTkFrame(master=frame_inferior, width=240, height=150, fg_color="#fff", border_color="#003b48", border_width=3)
    tarjeta_3.grid_propagate(0)
    tarjeta_3.grid(row=0, column=2, padx=(5, 10), pady=(10, 10))
    # Contenido de la tarjeta
    # Título
    silo_label3 = CTkLabel(master=tarjeta_3, text="Arroz blanco", font=("Poppins Medium", 18), text_color="#171717")
    silo_label3.grid(row=0, column=0, padx=(20, 0), pady=(15, 5), sticky="w")
    # Icono
    icon_img = Image.open("assets/icon-arroz.png").resize((20, 20))
    icon_photo = CTkImage(icon_img)
    icon_label = CTkLabel(master=tarjeta_3, image=icon_photo, text="")
    icon_label.grid(row=0, column=0, padx=(180, 0), pady=(10, 5), sticky="w")
    #------------------>
    # Información del silo 3
    # Toneladas
    toneladas_label3 = CTkLabel(master=tarjeta_3, text="Silo 2 y 3", font=("Poppins Light", 13), text_color="#171717")
    toneladas_label3.grid(row=1, column=0, padx=(20, 0), pady=(0, 0), sticky="w")
    toneladas_valor3 = CTkLabel(master=tarjeta_3, text="Disponibilidad: 3 toneladas", font=("Poppins Bold", 14), text_color="#ff3b3b")
    toneladas_valor3.grid(row=2, column=0, padx=(20, 0), pady=(0, 0), sticky="w")

    app.mainloop()

# Para ejecutar individualmente la ventana y testear
if __name__ == "__main__":
    listado_ordenes()