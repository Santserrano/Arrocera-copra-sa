from customtkinter import *
import tkinter as tk
from CTkTable import CTkTable
from PIL import Image, ImageTk

##################################################################################################

app = CTk()
app.geometry("856x645")
app.resizable(0,0)

set_appearance_mode("light")
app.config(bg="#f5ecdd") #Fondo beige

##################################################################################################
# Cargar imagen y convertirla a un objeto de imagen de tkinter
logistics_img_data = Image.open("assets/gerente_icon.png").convert("RGBA")
logistics_img = CTkImage(logistics_img_data, size=(100, 100))

# Definir color del botón y su tamaño
general_bloque = CTkButton(master=app, fg_color="#003b48", width=250, height=270, corner_radius=20, hover_color="#006278", text="Gerente General", text_color="#fff", font=("Poppins Bold", 20), image=logistics_img, compound="top")
general_bloque.grid_propagate(0)
general_bloque.pack(side="left", padx=(25, 0))

##################################################################################################

#Abro la imagen y redimenciono en 100x100
gerente_img_data = Image.open("assets/factory_icon.png").convert("RGBA")
gerente_img = CTkImage(gerente_img_data, size=(100, 100))

produccion_bloque = CTkButton(master=app, fg_color="#003b48", width=250, height=270, corner_radius=20, hover_color="#006278", text="Gerente Produccion", text_color="#fff", font=("Poppins Bold", 20), image=gerente_img, compound="top")
produccion_bloque.grid_propagate(0)
produccion_bloque.pack(side="left",expand=True, anchor="center")


##################################################################################################

transporte_img_data = Image.open("assets/path_icon.png").convert("RGBA")
transporte_img = CTkImage(transporte_img_data, size=(100, 100))

#Defino el color del bloque y su tamaño
transporte_bloque = CTkButton(master=app, fg_color="#003b48", width=250, height=270, corner_radius=20, hover_color="#006278", text="Gerente Transporte", text_color="#fff", font=("Poppins Bold", 20), image=transporte_img, compound="top")
transporte_bloque.grid_propagate(0)
transporte_bloque.pack(side="right", padx=(0, 25))

##################################################################################################

app.mainloop()