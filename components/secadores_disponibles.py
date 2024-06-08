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

def dashboard():
    ##################################################################################################
    app = CTk()
    app.geometry("856x645")
    app.resizable(0,0)

    app.iconbitmap('assets/logo.png') #Debe ser formato .ico :/
    app.title("Secadores Disponibles - Copra S.A")

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
    CTkLabel(master=title_frame, text="SECADORES DISPONIBLES", font=("Poppins Bold", 25), text_color="#003b48").grid(row=0, column=1, pady=(12, 0), sticky="n")
    CTkButton(master=title_frame, width=100, height=30, text="<  Volver", font=("Poppins Bold", 15), text_color="#fff", fg_color="#003b48", hover_color="#006278").grid(row=0, column=2, padx=(0, 10), sticky="e")
    
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
    table_frame.pack(expand=True, fill="both", padx=27, pady=21)
    table = CTkTable(master=table_frame, values=table_data, colors=["#007791", "#0299ba"], header_color="#003b48", hover_color="#006278")
    table.edit_row(0, text_color="#fff", hover_color="#006278", font=("Poppins Bold", 12))
    table.pack(expand=True)

    app.mainloop()

if __name__ == "__main__":
    dashboard()