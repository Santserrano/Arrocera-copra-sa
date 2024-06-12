from customtkinter import *
from PIL import Image, ImageTk
import os
from CTkTable import CTkTable
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter
import os

#------------------------------------------------------------------------------------------------------>
"""
Instancia de ventana,
color de fondo y logo.
"""

# Ventana
def pagos_transporte():

    def volver(root):
        root.destroy()
        from ID_log_2 import ID_log_2
        ID_log_2()

    app = CTk()
    app.geometry(f"{856}x{645}")
    app.resizable(0,0)
    app.title("Pagos y Documentación - Copra S.A")
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
    CTkLabel(master=title_frame, text="PAGOS Y DOCUMENTACIÓN", font=("Poppins Bold", 25), text_color="#003b48").grid(row=0, column=1, pady=(12, 0), sticky="n")
    CTkButton(master=title_frame, width=100, height=30, command=lambda: volver(app), text="<  Volver", font=("Poppins Bold", 15), text_color="#fff", fg_color="#003b48", hover_color="#006278").grid(row=0, column=2, padx=(0, 10), sticky="e")

    #------------------------------------------------------------------------------------------------------>
    table_data = [
        ["Fecha", "Monto", "Empresa", "Estado", "Factura"],
        ['2024-01-05', '$230.000', 'Arrocería El Granero Dorado', 'Entregado', 'Disponible'],
        ['2024-02-15', '$800.000', 'Molino Arrocero La Estrella', 'Pendiente', 'No Disponible'],
        ['2024-03-20', '$450.000', 'Arrozal San José', 'Pendiente', 'No Disponible'],
        ['2024-04-10', '$500.000', 'Arrozera Santa Isabel', 'Pendiente', 'No Disponible'],
        ['2024-05-18', '$720.000', 'Arrozales del Norte', 'Entregado', 'Disponible'],
        ['2024-06-25', '$950.000', 'Arrozales Hermanos García', 'Entregado', 'Disponible'],

    ]

    table_frame = CTkScrollableFrame(master=master_app, fg_color="transparent") # Frame con barra para deslizar
    table_frame.pack(expand=True, fill="both", pady=(0, 10))
    table = CTkTable(master=table_frame, values=table_data, colors=["#007791", "#0299ba"], header_color="#003b48", hover_color="#006278") # Objeto tabla
    table.edit_row(0, text_color="#fff", hover_color="#006278", font=("Poppins Bold", 12))
    table.pack(expand=True)

    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun']
    pagos = [15000, 18000, 20000, 22000, 25000, 23000]

    fig, ax = plt.subplots(figsize=(6.5, 3.5))
    ax.bar(meses, pagos, color='skyblue')
    ax.set_title('Reporte de Pagos Mensuales')
    ax.set_ylabel('Monto ($)')
    ax.grid(True)

    grafico = FigureCanvasTkAgg(fig, master=table_frame)
    grafico.draw()
    grafico.get_tk_widget().pack(pady=15)

    app.mainloop()

# Para ejecutar individualmente la ventana y testear
if __name__ == "__main__":
    pagos_transporte()