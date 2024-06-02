from customtkinter import *
import tkinter as tk
from CTkTable import CTkTable
from PIL import Image, ImageTk

##################################################################################################

app = CTk()
app.geometry("856x645")
app.resizable(0,0)

set_appearance_mode("light")
background_image = Image.open("assets/wall-back.png")
background_image = background_image.resize((856, 645))
background_photo = ImageTk.PhotoImage(background_image)

# Crear un Label para contener la imagen de fondo
background_label = tk.Label(app, image=background_photo)
background_label.place(relwidth=1, relheight=1)

##################################################################################################
# Cargar imagen y convertirla a un objeto de imagen de tkinter
logistics_img_data = Image.open("assets/id_log_transporte.png").convert("RGBA")
logistics_img = CTkImage(logistics_img_data, size=(100, 100))

# Definir color del botón y su tamaño
general_bloque = CTkButton(master=app, fg_color="#003b48", width=250, height=270, corner_radius=0, border_color="#fff", border_width=4, hover_color="#006278", text="Operaciones\n de transporte", text_color="#fff", font=("Poppins Bold", 20), image=logistics_img, compound="top")
general_bloque.grid_propagate(0)
general_bloque.pack(side="left", padx=(25, 0))

##################################################################################################

#Abro la imagen y redimenciono en 100x100
gerente_img_data = Image.open("assets/id_log_rutas.png").convert("RGBA")
gerente_img = CTkImage(gerente_img_data, size=(100, 100))

produccion_bloque = CTkButton(master=app, fg_color="#003b48", width=250, height=270, corner_radius=0, border_color="#fff", border_width=4, hover_color="#006278", text="Recorridos", text_color="#fff", font=("Poppins Bold", 20), image=gerente_img, compound="top")
produccion_bloque.grid_propagate(0)
produccion_bloque.pack(side="left",expand=True, anchor="center")


##################################################################################################

transporte_img_data = Image.open("assets/id_log_pagos.png").convert("RGBA")
transporte_img = CTkImage(transporte_img_data, size=(100, 100))

#Defino el color del bloque y su tamaño
transporte_bloque = CTkButton(master=app, fg_color="#003b48", width=250, height=270, corner_radius=0, border_color="#fff", border_width=4, hover_color="#006278", text="Pagos y\n documentación", text_color="#fff", font=("Poppins Bold", 20), image=transporte_img, compound="top")
transporte_bloque.grid_propagate(0)
transporte_bloque.pack(side="right", padx=(0, 25))

##################################################################################################

app.mainloop()