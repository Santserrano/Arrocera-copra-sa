import tkinter
import tkintermapview
from customtkinter import *
from PIL import Image, ImageTk
import os
from CTkTable import CTkTable
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#------------------------------------------------------------------------------------------------------>
"""
Instancia de ventana,
color de fondo y logo.
"""

# Ventana
def ops_transporte():

    def gerente_config(root): # Secadores disponibles - Secado de arroz - Lista tabla
        from config_acc import config_acc
        root.destroy()
        config_acc()

    def volver(root):
        root.destroy()
        from ID_log_2 import ID_log_2
        ID_log_2()

    app = CTk()
    app.geometry(f"{856}x{645}")
    app.resizable(0,0)
    app.title("Operaciones de Transporte - Copra S.A")
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
    CTkLabel(master=title_frame, text="OPERACIONES TRANSPORTE", font=("Poppins Bold", 25), text_color="#003b48").grid(row=0, column=1, padx=(90, 0), pady=(12, 0), sticky="n")
    CTkButton(master=title_frame, width=100, height=30, command=lambda: gerente_config(app), text="* Cuenta", font=("Poppins Bold", 15), text_color="#fff", fg_color="#003b48", hover_color="#006278").grid(row=0, column=2, padx=(0, 10), sticky="e")
    CTkButton(master=title_frame, width=100, height=30, command=lambda: volver(app), text="<  Volver", font=("Poppins Bold", 15), text_color="#fff", fg_color="#003b48", hover_color="#006278").grid(row=0, column=3, padx=(0, 10), sticky="e")

    table_data = [
        ["Conductor", "Fecha", "Ruta", "Tiempo", "Estado"],
        ['Juan Pérez', '2024-01-05', '2', '4 horas', 'Entregado'],
        ['María Gómez', '2024-02-15', '3', '5 horas', 'Pendiente'],
        ['Pedro Rodríguez', '2024-03-20', '1', '3 horas', 'Entregado'],
        ['Ana López', '2024-04-10', '1', '6 horas', 'Entregado'],
        ['Luis Martínez', '2024-05-18', '3', '5.5 horas', 'Entregado'],
        ['Sofía Fernández', '2024-06-25', '2', '7 horas', 'Pendiente'],
    ]

    table_frame = CTkScrollableFrame(master=master_app, fg_color="transparent")
    table_frame.pack(expand=True, fill="both", pady=(0, 10))
    table = CTkTable(master=table_frame, values=table_data, colors=["#007791", "#0299ba"], header_color="#003b48", hover_color="#006278")
    table.edit_row(0, text_color="#fff", hover_color="#006278", font=("Poppins Bold", 12))
    table.pack(expand=True)
    #------------------------------------------------------------------------------------------------------>
    # Datos de ejemplo para el gráfico
    dias = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    tiempo_promedio_entrega = [4, 3, 5, 4.5, 3.8, 4, 3, 5, 4.5, 3.8, 4, 3]  # Tiempo en horas

    # Se crea la figura y asignan etiquetas
    fig, ax = plt.subplots(figsize=(6.5, 3.5))
    ax.plot(dias, tiempo_promedio_entrega, marker='o', color='b')
    ax.set_title('Tiempo promedio entregas')
    ax.set_ylabel('Tiempo promedio (horas)')
    ax.grid(True)

    grafico = FigureCanvasTkAgg(fig, master=table_frame)
    grafico.draw()
    grafico.get_tk_widget().pack()

    app.mainloop()

if __name__ == "__main__":
    ops_transporte()