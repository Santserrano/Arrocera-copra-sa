import tkinter
import tkintermapview
from customtkinter import *
from PIL import Image, ImageTk
import os

#------------------------------------------------------------------------------------------------------>
"""
Instancia de ventana,
color de fondo y logo.
"""
# Ventana
app = tkinter.Tk()
app.geometry(f"{856}x{645}")
app.resizable(0,0)
app.title("Operaciones de Transporte - Copra S.A")
logo_img_data = Image.open("assets/logo.png")

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
CTkLabel(master=title_frame, text="OPERACIONES DE TRANSPORTE", font=("Poppins Bold", 25), text_color="#003b48").grid(row=0, column=1, pady=(12, 0), sticky="n")
CTkButton(master=title_frame, width=100, height=30, text="<  Volver", font=("Poppins Bold", 15), text_color="#fff", fg_color="#003b48", hover_color="#006278").grid(row=0, column=2, padx=(0, 10), sticky="e")

#------------------------------------------------------------------------------------------------------>




app.mainloop()