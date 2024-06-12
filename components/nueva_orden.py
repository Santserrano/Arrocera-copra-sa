from customtkinter import *
import tkinter
from PIL import Image
import sqlite3
import random


def nueva_orden():

    app = CTk()
    app.geometry("856x645")
    app.resizable(0,0)

    def volver(root):
        from dashboard import dashboard
        root.destroy()
        dashboard()

    #------------------------------------------------------------------------------------------------>  
    """
    FUNCIONES BOTONES
    """
    ########################################## CONEXIÓN CON BASE DE DATOS #############################################
    def insertar_orden(item, cliente, direccion, estado, cantidad):
        nro = random.randint(1, 5000)
        
        conn = sqlite3.connect('ordenes.db')
        c = conn.cursor()

        c.execute('INSERT INTO ordenes (nro, item, cliente, direccion, estado, cantidad) VALUES (?, ?, ?, ?, ?, ?)', (nro, item, cliente, direccion, estado, cantidad))

        conn.commit()
        conn.close()

        n_item.delete(0, END)
        n_cliente.delete(0, END)
        n_direccion.delete(0, END)
        n_descripcion.delete(0, END)
    #######################################################################################
    def panel_principal(root):
        from dashboard import dashboard
        root.destroy()
        dashboard()

    def ordenes(root):
        from ordenes_gerente import ordenes_gerente
        root.destroy()
        ordenes_gerente()
    
    def gerente_config(root):
        from config_acc import config_acc
        root.destroy()
        config_acc()
    
    def usuarios_config(root):
        from config_usuarios import config_usuarios
        root.destroy()
        config_usuarios()
    #------------------------------------------------------------------------------------------------>

    # Centrar ventana
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    window_width = 856
    window_height = 645
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2 - 50
    # Centro del escritorio
    app.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
    app.title("Nueva Orden - Copra S.A")

    sidebar_frame = CTkFrame(master=app, fg_color="#003b48",  width=176, height=650, corner_radius=0)
    sidebar_frame.pack_propagate(0)
    sidebar_frame.pack(fill="y", anchor="w", side="left")

    logo_img_data = Image.open("assets/logo.png")
    app.iconbitmap('assets/logo.ico')
    logo_img = CTkImage(light_image=logo_img_data, size=(77.68, 85.42))

    CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")

    analytics_img_data = Image.open("assets/analytics_icon.png")
    analytics_img = CTkImage(analytics_img_data)

    CTkButton(master=sidebar_frame, image=analytics_img, command=lambda: panel_principal(app), text="Panel Principal", fg_color="transparent", font=("Poppins Bold", 14), hover_color="#006278", anchor="w").pack(anchor="center", ipady=5, pady=(60, 0))

    package_img_data = Image.open("assets/package_icon.png")
    package_img = CTkImage(package_img_data)

    CTkButton(master=sidebar_frame, image=package_img, text="Crear Orden", fg_color="#fff", font=("Poppins Bold", 14), text_color="#003b48", hover_color="#eee", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

    list_img_data = Image.open("assets/list_icon.png")
    list_img = CTkImage(list_img_data)
    CTkButton(master=sidebar_frame, image=list_img, command=lambda: ordenes(app), text="Ordenes", fg_color="transparent", font=("Poppins Bold", 14), hover_color="#006278", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

    settings_img_data = Image.open("assets/settings_icon.png")
    settings_img = CTkImage(settings_img_data)
    CTkButton(master=sidebar_frame, image=settings_img, command=lambda: usuarios_config(app), text="Configuración", fg_color="transparent", font=("Poppins Bold", 14), hover_color="#006278", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

    person_img_data = Image.open("assets/person_icon.png")
    person_img = CTkImage(person_img_data)
    CTkButton(master=sidebar_frame, image=person_img, command=lambda: gerente_config(app), text="Cuenta", fg_color="transparent", font=("Poppins Bold", 14), hover_color="#006278", anchor="w").pack(anchor="center", ipady=5, pady=(160, 0))

    main_view = CTkFrame(master=app, fg_color="#fff",  width=680, height=650, corner_radius=0)
    main_view.pack_propagate(0)
    main_view.pack(side="left")

    CTkLabel(master=main_view, text="Generar Orden", font=("Poppins Bold", 25), text_color="#003b48").pack(anchor="nw", pady=(29,0), padx=27)

    CTkLabel(master=main_view, text="Nombre Item", font=("Poppins Bold", 17), text_color="#003b48").pack(anchor="nw", pady=(25,0), padx=27)

    n_item = CTkEntry(master=main_view, fg_color="#003b48", border_width=0)
    n_item.pack(fill="x", pady=(12,0), padx=27, ipady=10)


    grid = CTkFrame(master=main_view, fg_color="transparent")
    grid.pack(fill="both", padx=27, pady=(31,0))

    CTkLabel(master=grid, text="Cliente", font=("Poppins Bold", 17), text_color="#003b48", justify="left").grid(row=0, column=0, sticky="w")
    n_cliente = CTkEntry(master=grid, fg_color="#003b48", border_width=0, width=300)
    n_cliente.grid(row=1, column=0, ipady=10)

    CTkLabel(master=grid, text="Dirección", font=("Poppins Bold", 17), text_color="#003b48", justify="left").grid(row=0, column=1, sticky="w", padx=(25,0))
    n_direccion = CTkEntry(master=grid, fg_color="#003b48", border_width=0, width=300)
    n_direccion.grid(row=1, column=1, ipady=10, padx=(24,0))

    CTkLabel(master=grid, text="Estado", font=("Poppins Bold", 17), text_color="#003b48", justify="left").grid(row=2, column=0, sticky="w", pady=(33, 0), padx=(0,25))
    n_descripcion = CTkEntry(master=grid, fg_color="#003b48", width=300, corner_radius=8)
    n_descripcion.grid(row=3, column=0, rowspan=5, sticky="w", pady=(16, 0), padx=(0,0))

    CTkLabel(master=grid, text="Cantidad", font=("Poppins Bold", 17), text_color="#003b48", justify="left").grid(row=2, column=1, sticky="w", pady=(33, 0), padx=(25,0))
    n_cantidad = CTkEntry(master=grid, fg_color="#003b48", width=300, corner_radius=8)
    n_cantidad.grid(row=3, column=1, rowspan=5, sticky="w", pady=(16, 0), padx=(24,0))

    actions= CTkFrame(master=main_view, fg_color="transparent")
    actions.pack(fill="both")

    CTkButton(master=actions, text="Volver", width=300, command=lambda: volver(app), fg_color="transparent", font=("Poppins Bold", 17), border_color="#003b48", hover_color="#eee", border_width=2, text_color="#003b48").pack(side="left", anchor="sw", pady=(25,0), padx=(27,24))
    CTkButton(master=actions, text="Crear", width=300, command=lambda: insertar_orden(n_item.get(), n_cliente.get(), n_direccion.get(), n_descripcion.get(), n_cantidad.get()), font=("Poppins Bold", 17), hover_color="#006278", fg_color="#003b48", text_color="#fff").pack(side = "left", anchor="se", pady=(25,0), padx=(0,27))
    
    app.mainloop()

if __name__ == "__main__":
    nueva_orden()