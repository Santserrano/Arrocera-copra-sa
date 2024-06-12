from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
import sys
import os
#from engine.functions import RecepcionArroz, CargaDescarga, Almacenamiento, Secado, Mantenimiento, NuevaOrden

#Configuración del PATH de engine para importaciones absolutas
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_dir)

def ordenes_gerente():
    ##################################################################################################

    def volver(root):
        from dashboard import dashboard
        root.destroy()
        dashboard()

    app = CTk()
    app.geometry("856x645")
    app.resizable(0,0)

    app.iconbitmap('assets/logo.png') #Debe ser formato .ico :/
    app.title("Listado Ordenes - Copra S.A")

    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    window_width = 856
    window_height = 645
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2 - 50
    # Centro del escritorio
    app.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")


    logo_img_data = Image.open("assets/logo.png") #Carga del logo
    logo_img = CTkImage(logo_img_data, size=(50, 55)) #Redimensionamiento del logo

    ###################################### ------------>SE DEFINE EL BLOQUE IZQUIERDO <------------ ######################################
    main_view = CTkFrame(master=app, fg_color="#fff",  width=856, height=645, corner_radius=0)
    main_view.pack_propagate(0)
    main_view.pack(side="top")

    title_frame = CTkFrame(master=main_view, fg_color="#d9ecec")
    title_frame.pack(fill="x", pady=(0, 10), ipady=3)

    # Configuración de las columnas del grid
    title_frame.columnconfigure(0, weight=1)
    title_frame.columnconfigure(1, weight=1)
    title_frame.columnconfigure(2, weight=1)

    CTkLabel(master=title_frame, text="", image=logo_img).grid(row=0, column=0, padx=(10, 0), pady=(3, 0), sticky="w")
    CTkLabel(master=title_frame, text="LISTADO ORDENES", font=("Poppins Bold", 25), text_color="#003b48").grid(row=0, column=1, pady=(12, 0), sticky="n")
    CTkButton(master=title_frame, width=100, height=30, command=lambda: volver(app), text="<  Volver", font=("Poppins Bold", 15), text_color="#fff", fg_color="#003b48", hover_color="#006278").grid(row=0, column=2, padx=(0, 10), sticky="e")
    
    ###################################### ------------> SE DEFINE EL BLOQUE DE ORDENES Y LISTA DE CLIENTES <------------ ######################################
    table_data = [
        ["Modelo", "Capacidades m3", "Temperatura °C", "Energía kcal/h", "Consumo de combustible GLP"],
        ['KW 500', '45', '60', '850000', '67'],
        ['KW 1000', '89', '38', '16900000', '134'],
        ['KW 1400', '117', '39', '221000000', '175'],
        ['KW 2000', '159', '60', '290000000', '230'],
        ['KW 2300', '191', '60', '371000000', '294'],
        ['KW 3000', '245', '39', '495000000', '393'],

    ]

    table_frame = CTkScrollableFrame(master=main_view, fg_color="transparent")
    table_frame.pack(expand=True, fill="both", padx=27, pady=3)
    table = CTkTable(master=table_frame, values=table_data, colors=["#007791", "#0299ba"], header_color="#003b48", hover_color="#006278")
    table.edit_row(0, text_color="#fff", hover_color="#006278", font=("Poppins Bold", 12))
    table.pack(expand=True)

    frame_inferior = CTkFrame(master=main_view, fg_color="#0299ba", width=856, height=400)
    frame_inferior.pack(expand=True, padx=10, pady=(0, 120), side="top")

    tarjeta_1 = CTkFrame(master=frame_inferior, width=240, height=150, fg_color="#fff", corner_radius=35, border_color="#003b48", border_width=3)
    tarjeta_1.grid_propagate(0)
    tarjeta_1.pack(expand=True, anchor="center", padx=(0, 10))
    # Contenido de la tarjeta
    # Título
    silo_label = CTkLabel(master=tarjeta_1, text="Silo 1", font=("Poppins Medium", 18), text_color="#171717")
    silo_label.grid(row=0, column=0, padx=(20, 0), pady=(15, 5), sticky="w")
    # Icono
    icon_img = Image.open("assets/icon-arroz.png").resize((20, 20))
    icon_photo = CTkImage(icon_img)
    icon_label = CTkLabel(master=tarjeta_1, image=icon_photo, text="")
    icon_label.grid(row=0, column=1, padx=(0, 30), pady=(10, 5), sticky="w")
    #------------------>
    # Información del silo 1
    # Toneladas
    toneladas_label = CTkLabel(master=tarjeta_1, text="Capacidad: 50 toneladas", font=("Poppins Light", 13), text_color="#171717")
    toneladas_label.grid(row=1, column=0, padx=(20, 0), pady=(0, 0), sticky="w")
    toneladas_valor = CTkLabel(master=tarjeta_1, text="Próxima limpieza: 5 días", font=("Poppins Bold", 14), text_color="#ff3b3b")
    toneladas_valor.grid(row=2, column=0, padx=(20, 0), pady=(0, 0), sticky="w")
    
    estado_label = CTkLabel(master=tarjeta_1, text="Limpiar", font=("Poppins Medium", 14), fg_color="#003b48", corner_radius=25, width=74, height=25, text_color="#fff")
    estado_label.grid(row=3, column=0, padx=(20, 0), pady=(5, 0), sticky="w")

    app.mainloop()

if __name__ == "__main__":
    ordenes_gerente()