from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
import sys
import os
import tkinter as tk
import sqlite3

#Configuración del PATH de engine para importaciones absolutas
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_dir)

def dashboard():
    ##################################################################################################
    app = CTk()
    app.geometry("856x645")
    app.resizable(0,0)
    # Centrar ventana
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    window_width = 856
    window_height = 645
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2 - 50
    # Centro del escritorio
    app.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    #------------------------------------------------------------------------------------------------>  
    """
    FUNCIONES BOTONES
    """
    def nueva_orden(root): # Secadores disponibles - Secado de arroz - Lista tabla
        from nueva_orden import nueva_orden
        root.destroy()
        nueva_orden()

    def ventana_ordenes(root): # Secadores disponibles - Secado de arroz - Lista tabla
        from listado_ordenes import listado_ordenes
        root.destroy()
        listado_ordenes()
    
    def gerente_config(root): # Secadores disponibles - Secado de arroz - Lista tabla
        from config_acc import config_acc
        root.destroy()
        config_acc()
    
    def generar_factura(): # Secadores disponibles - Secado de arroz - Lista tabla
        from test_facturacion import generar_factura
        generar_factura()
    #------------------------------------------------------------------------------------------------>
    app.iconbitmap('assets/logo.ico')
    app.title("Agrorice - Copra S.A")

    sidebar_frame = CTkFrame(master=app, fg_color="#003b48",  width=176, height=650, corner_radius=0) #Bloque izquierdo
    sidebar_frame.pack_propagate(0)
    sidebar_frame.pack(fill="y", anchor="w", side="left") #Bloque en el lado izquierdo

    logo_img_data = Image.open("assets/logo.png") #Carga del logo
    logo_img = CTkImage(logo_img_data, size=(90, 100)) #Redimensionamiento del logo

    CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center") #Inserción del logo como etiqueta

    analytics_img_data = Image.open("assets/analytics_icon.png")
    analytics_img = CTkImage(analytics_img_data)

    CTkButton(master=sidebar_frame, image=analytics_img, text="Panel Principal", fg_color="#fff", text_color="#003b48", font=("Poppins Bold", 14), hover_color="#006278", anchor="w").pack(anchor="center", ipady=5, pady=(60, 0))

    package_img_data = Image.open("assets/package_icon.png")
    package_img = CTkImage(package_img_data)
    ###################################### SE DEFINEN LOS BOTONES DEL LADO IZQUIERDO Y SE CARGAN SUS RESPECTIVOS ICONOS ######################################
    
    CTkButton(master=sidebar_frame, image=package_img, text="Ordenar", command=lambda: nueva_orden(app), fg_color="transparent", font=("Poppins Bold", 14), text_color="#fff", hover_color="#006278", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))
    
    #########################################################################################################
    
    list_img_data = Image.open("assets/list_icon.png")
    list_img = CTkImage(list_img_data)
    CTkButton(master=sidebar_frame, image=list_img, command=lambda: ventana_ordenes(app), text="Ordenes", fg_color="transparent", font=("Poppins Bold", 14), hover_color="#006278", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

    #########################################################################################################
    
    settings_img_data = Image.open("assets/settings_icon.png")
    settings_img = CTkImage(settings_img_data)
    CTkButton(master=sidebar_frame, image=settings_img, text="Reporte PDF", command=lambda: generar_factura(), fg_color="transparent", font=("Poppins Bold", 14), hover_color="#006278", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

    #########################################################################################################
    
    person_img_data = Image.open("assets/person_icon.png")
    person_img = CTkImage(person_img_data)
    CTkButton(master=sidebar_frame, image=person_img, command=lambda: gerente_config(app), text="Cuenta", fg_color="transparent", font=("Poppins Bold", 14), hover_color="#006278", anchor="w").pack(anchor="center", ipady=8, pady=(120, 0))

    ###################################### ------------>SE DEFINE EL BLOQUE IZQUIERDO <------------ ######################################
    main_view = CTkFrame(master=app, fg_color="#fff",  width=680, height=650, corner_radius=0)
    main_view.pack_propagate(0)
    main_view.pack(side="right")

    title_frame = CTkFrame(master=main_view, fg_color="transparent")
    title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

    CTkLabel(master=title_frame, text="Menú principal", font=("Poppins Bold", 25), text_color="#003b48").pack(anchor="nw", side="left")

    CTkButton(master=title_frame, command=lambda: nueva_orden(app), text="+ Nueva Orden",  font=("Poppins Bold", 15), text_color="#fff", fg_color="#003b48", hover_color="#006278").pack(anchor="ne", side="right")

    metrics_frame = CTkFrame(master=main_view, fg_color="transparent")
    metrics_frame.pack(anchor="n", fill="x",  padx=27, pady=(36, 0))

    orders_metric = CTkFrame(master=metrics_frame, fg_color="#003b48", width=200, height=60)
    orders_metric.grid_propagate(0)
    orders_metric.pack(side="left")

    logitics_img_data = Image.open("assets/gerente_icon.png")
    logistics_img = CTkImage(logitics_img_data, size=(43, 43))

    CTkLabel(master=orders_metric, image=logistics_img, text="").grid(row=0, column=0, rowspan=2, padx=(12,5), pady=10)

    CTkLabel(master=orders_metric, text="Ordenes", text_color="#fff", font=("Poppins Bold", 15)).grid(row=0, column=1, sticky="sw")
    CTkLabel(master=orders_metric, text="123", text_color="#fff",font=("Poppins Bold", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0,10))


    shipped_metric = CTkFrame(master=metrics_frame, fg_color="#003b48", width=200, height=60)
    shipped_metric.grid_propagate(0)
    shipped_metric.pack(side="left",expand=True, anchor="center")

    shipping_img_data = Image.open("assets/factory_icon.png")
    shipping_img = CTkImage(shipping_img_data, size=(43, 43))

    CTkLabel(master=shipped_metric, image=shipping_img, text="").grid(row=0, column=0, rowspan=2, padx=(12,5), pady=10)

    CTkLabel(master=shipped_metric, text="Pendientes", text_color="#fff", font=("Poppins Bold", 15)).grid(row=0, column=1, sticky="sw")
    CTkLabel(master=shipped_metric, text="91", text_color="#fff",font=("Poppins Bold", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0,10))

    delivered_metric = CTkFrame(master=metrics_frame, fg_color="#003b48", width=200, height=60)
    delivered_metric.grid_propagate(0)
    delivered_metric.pack(side="right",)

    delivered_img_data = Image.open("assets/path_icon.png")
    delivered_img = CTkImage(delivered_img_data, size=(43, 43))

    CTkLabel(master=delivered_metric, image=delivered_img, text="").grid(row=0, column=0, rowspan=2, padx=(12,5), pady=10)

    CTkLabel(master=delivered_metric, text="Enviados", text_color="#fff", font=("Poppins Bold", 15)).grid(row=0, column=1, sticky="sw")
    CTkLabel(master=delivered_metric, text="23", text_color="#fff",font=("Poppins Bold", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0,10))

    search_container = CTkFrame(master=main_view, height=50, fg_color="#F0F0F0")
    search_container.pack(fill="x", pady=(45, 0), padx=27)

    ###################################### ------------> SE DEFINE EL BLOQUE DE ORDENES Y LISTA DE CLIENTES <------------ ######################################
    CTkEntry(master=search_container, width=305, placeholder_text="Buscar orden", border_color="#003b48", border_width=2).pack(side="left", padx=(13, 0), pady=15)

    CTkComboBox(master=search_container, width=125, values=["Fecha", "Más reciente", "Últimas entregas"], button_color="#003b48", border_color="#003b48", border_width=2, button_hover_color="#006278",dropdown_hover_color="#006278" , dropdown_fg_color="#003b48", dropdown_text_color="#fff").pack(side="left", padx=(13, 0), pady=15)
    CTkComboBox(master=search_container, width=125, values=["Estado", "En proceso", "Enviado", "Entregado", "Pendiente", "Cancelado"], button_color="#003b48", border_color="#003b48", border_width=2, button_hover_color="#006278",dropdown_hover_color="#006278" , dropdown_fg_color="#003b48", dropdown_text_color="#fff").pack(side="left", padx=(13, 0), pady=15)

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

    table_frame = CTkScrollableFrame(master=main_view, fg_color="transparent")
    table_frame.pack(expand=True, fill="both", padx=27, pady=21)
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
    #################################

    app.mainloop()

if __name__ == "__main__":
    dashboard()