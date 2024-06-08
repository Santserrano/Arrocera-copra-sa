import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from customtkinter import *
import os

# Instancia de ventana
app = tk.Tk()
app.geometry("856x645")
app.resizable(0, 0)
app.title("Almacenamiento - Copra S.A")

# Fondo azul marino
master_app = CTkFrame(master=app, fg_color="#003b48", width=856, height=645)
master_app.pack_propagate(0)
master_app.pack(expand=True)

# Frame para la fila superior
frame_superior = CTkFrame(master=master_app, fg_color="transparent")
frame_superior.pack(fill="both", expand=True, padx=20, pady=(20, 5))





# --------------------------------------------- TARJETA SILO 1 ---------------------------------------------
tarjeta_1 = CTkFrame(master=frame_superior, width=343, height=190, fg_color="#fff", corner_radius=35)
tarjeta_1.grid_propagate(0)
tarjeta_1.pack(side="left", expand=True, anchor="center", padx=(50, 10))
# Contenido de la tarjeta
# Título
silo_label = CTkLabel(master=tarjeta_1, text="Silo 1", font=("Poppins Medium", 18), text_color="#171717")
silo_label.grid(row=0, column=0, padx=(20, 0), pady=(15, 5), sticky="w")
# Icono
icon_img = Image.open("assets/icon-arroz.png").resize((20, 20))
icon_photo = CTkImage(icon_img)
icon_label = CTkLabel(master=tarjeta_1, image=icon_photo, text="")
icon_label.grid(row=0, column=1, padx=(0, 5), pady=(10, 5), sticky="w")
# Estado
estado_label = CTkLabel(master=tarjeta_1, text="Óptimo", font=("Poppins Medium", 14), fg_color="#B6F6B5", corner_radius=30, width=74, height=25, text_color="#74bd73")
estado_label.grid(row=0, column=2, padx=(110, 5), pady=(10, 5), sticky="e")
#------------------>
# Información del silo 1
# Toneladas
toneladas_label = CTkLabel(master=tarjeta_1, text="Toneladas", font=("Poppins Light", 13), text_color="#171717")
toneladas_label.grid(row=1, column=0, padx=(20, 0), pady=(0, 0), sticky="w")
toneladas_valor = CTkLabel(master=tarjeta_1, text="25", font=("Poppins Bold", 14), text_color="#171717")
toneladas_valor.grid(row=2, column=0, padx=(20, 0), pady=(0, 0), sticky="w")
# Tiempo
tiempo_label = CTkLabel(master=tarjeta_1, text="Tiempo", font=("Poppins Light", 13), text_color="#171717")
tiempo_label.grid(row=3, column=0, padx=(20, 0), pady=(10, 0), sticky="w")
tiempo_valor = ctk.CTkLabel(master=tarjeta_1, text="2 días", font=("Poppins Bold", 14), text_color="#171717")
tiempo_valor.grid(row=4, column=0, padx=(20, 0), pady=(0, 10), sticky="w")
# Humedad
humedad_label = CTkLabel(master=tarjeta_1, text="Humedad", font=("Poppins Light", 13), text_color="#171717")
humedad_label.grid(row=1, column=2, padx=(100, 20), pady=(0, 0), sticky="w")
humedad_valor = CTkLabel(master=tarjeta_1, text="12.5%", font=("Poppins Bold", 14), text_color="#171717")
humedad_valor.grid(row=2, column=2, padx=(100, 20), pady=(0, 0), sticky="w")
# Temperatura
temperatura_label = CTkLabel(master=tarjeta_1, text="Temperatura", font=("Poppins Light", 13), text_color="#171717")
temperatura_label.grid(row=3, column=2, padx=(100, 20), pady=(10, 0), sticky="w")
temperatura_valor = CTkLabel(master=tarjeta_1, text="24.2°C", font=("Poppins Bold", 14), text_color="#171717")
temperatura_valor.grid(row=4, column=2, padx=(100, 20), pady=(0, 10), sticky="w")




app.mainloop()
