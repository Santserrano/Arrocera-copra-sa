from customtkinter import *
from PIL import Image
from CTkTable import CTkTable

#------------------------------------------------------------------------------------------------------>
# Ventana
def carga_y_descarga():

    def volver(root):
        from ID_log import ID_log
        root.destroy()
        ID_log()

    """
    Instancia de ventana,
    color de fondo y logo.
    """

    app = CTk()
    app.geometry(f"{856}x{645}")
    app.resizable(0,0)
    app.title("Carga y descarga de camiones - Copra S.A")
    logo_img_data = Image.open("assets/logo.png")

    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    window_width = 856
    window_height = 645
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2 - 50
    # Centro del escritorio
    app.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    # Logo volver
    returns_img_data = Image.open("assets/returns_icon.png")
    returns_img = CTkImage(returns_img_data)

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
    CTkLabel(master=title_frame, text="CARGA Y DESCARGA DE CAMIONES", font=("Poppins Bold", 25), text_color="#003b48").grid(row=0, column=1, pady=(12, 0), sticky="n")
    CTkButton(master=title_frame, width=100, height=30, command=lambda: volver(app), text="<  Volver", font=("Poppins Bold", 15), text_color="#fff", fg_color="#003b48", hover_color="#006278").grid(row=0, column=2, padx=(0, 10), sticky="e")

    #------------------------------------------------------------------------------------------------------>
    table_data = [
        ["Conductor", "Fecha", "Ruta", "Tiempo", "Estado"],
        ['Juan Pérez', '2024-01-05', '2', '4 horas', 'Entregado'],
        ['María Gómez', '2024-02-15', '3', '5 horas', 'Pendiente'],
        ['Pedro Rodríguez', '2024-03-20', '1', '3 horas', 'Entregado'],
        ['Ana López', '2024-04-10', '1', '6 horas', 'Entregado'],
        ['Luis Martínez', '2024-05-18', '3', '5.5 horas', 'Entregado'],
        ['Sofía Fernández', '2024-06-25', '2', '7 horas', 'Pendiente'],
        ['Augusto Ojeda', '2024-09-05', '2', '4 horas', 'Entregado'],
        ['Agustín Caceres', '2024-11-15', '3', '5 horas', 'Pendiente'],
        ['Felipe Rodríguez', '2024-12-20', '1', '3 horas', 'Entregado'],
    ]

    table_frame = CTkScrollableFrame(master=master_app, fg_color="transparent")
    table_frame.pack(expand=True, fill="both")
    table = CTkTable(master=table_frame, values=table_data, colors=["#007791", "#0299ba"], header_color="#003b48", hover_color="#006278")
    table.edit_row(0, text_color="#fff", hover_color="#006278", font=("Poppins Bold", 12))
    table.pack(expand=True)

    frame_inferior = CTkFrame(master=master_app, fg_color="#0299ba", width=856, height=280)
    frame_inferior.pack(expand=True, pady=(0, 60), side="top")

    # Datos de ejemplo para las tarjetas
    camiones = [
        {"titulo": "Camión 1", "capacidad": "Capacidad: 20 toneladas", "estado": "Cargando"},
        {"titulo": "Camión 2", "capacidad": "Capacidad: 25 toneladas", "estado": "En camino"},
        {"titulo": "Camión 3", "capacidad": "Capacidad: 18 toneladas", "estado": "Descargando"},
    ]

    for i, camion in enumerate(camiones):
        tarjeta = CTkFrame(master=frame_inferior, width=240, height=150, fg_color="#fff", border_color="#003b48", border_width=3)
        tarjeta.grid_propagate(0)
        tarjeta.pack(expand=True, side="left", padx=(0, 0))
        
        # data de la tarjeta
        camion_label = CTkLabel(master=tarjeta, text=camion["titulo"], font=("Poppins Medium", 18), text_color="#171717")
        camion_label.grid(row=0, column=0, padx=(20, 0), pady=(15, 5), sticky="w")
        
        icon_img = Image.open("assets/icon-camion.png").resize((20, 20))
        icon_photo = CTkImage(icon_img)
        icon_label = CTkLabel(master=tarjeta, image=icon_photo, text="")
        icon_label.grid(row=0, column=1, padx=(0, 30), pady=(10, 5), sticky="w")
        
        capacidad_label = CTkLabel(master=tarjeta, text=camion["capacidad"], font=("Poppins Light", 13), text_color="#171717")
        capacidad_label.grid(row=1, column=0, padx=(20, 0), pady=(0, 0), sticky="w")
        
        estado_label = CTkLabel(master=tarjeta, text=camion["estado"], font=("Poppins Medium", 14), fg_color="#003b48", corner_radius=25, width=100, height=25, text_color="#fff")
        estado_label.grid(row=2, column=0, padx=(20, 0), pady=(5, 0), sticky="w")

    app.mainloop()

if __name__ == "__main__":
    carga_y_descarga()