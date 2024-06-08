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
app.title("Almacenamiento - Copra S.A")
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
CTkLabel(master=title_frame, text="ALMACENAMIENTO DE ARROZ", font=("Poppins Bold", 25), text_color="#003b48").grid(row=0, column=1, pady=(12, 0), sticky="n")
CTkButton(master=title_frame, width=100, height=30, text="<  Volver", font=("Poppins Bold", 15), text_color="#fff", fg_color="#003b48", hover_color="#006278").grid(row=0, column=2, padx=(0, 10), sticky="e")

#------------------------------------------------------------------------------------------------------>
"""
Grilla de las 4 tarjetas
correspondiente a cada silo.
"""
# Frame para la fila superior !!!
frame_superior = CTkFrame(master=master_app, fg_color="transparent", width=856, height=400)
frame_superior.pack(expand=True, padx=10, pady=(80, 10))

# Tarjeta superior izquierda
#B6F6B5 verde agua <> #992929 rojo <> ##999529 amarillo

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
tiempo_valor = CTkLabel(master=tarjeta_1, text="2 días", font=("Poppins Bold", 14), text_color="#171717")
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


# --------------------------------------------- TARJETA SILO 2 ---------------------------------------------
tarjeta_1 = CTkFrame(master=frame_superior, width=343, height=190, fg_color="#fff", corner_radius=35)
tarjeta_1.grid_propagate(0)
tarjeta_1.pack(side="right", expand=True, anchor="center", padx=(10, 50))
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
tiempo_valor = CTkLabel(master=tarjeta_1, text="2 días", font=("Poppins Bold", 14), text_color="#171717")
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




"""
Grilla inferior de 2 tarjetas
correspondiente a los silos de abajo
"""

#------------------------------------------------------------------------------------------------------>

# Frame para la fila inferior !!!
frame_inferior = CTkFrame(master=master_app, fg_color="transparent", width=856, height=400)
frame_inferior.pack(expand=True, padx=10, pady=(0, 100))

# --------------------------------------------- TARJETA SILO 3 ---------------------------------------------
tarjeta_1 = CTkFrame(master=frame_inferior, width=343, height=190, fg_color="#fff", corner_radius=35)
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
tiempo_valor = CTkLabel(master=tarjeta_1, text="2 días", font=("Poppins Bold", 14), text_color="#171717")
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

# --------------------------------------------- TARJETA SILO 4 ---------------------------------------------
tarjeta_1 = CTkFrame(master=frame_inferior, width=343, height=190, fg_color="#fff", corner_radius=35)
tarjeta_1.grid_propagate(0)
tarjeta_1.pack(side="right", expand=True, anchor="center", padx=(10, 50))
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
tiempo_valor = CTkLabel(master=tarjeta_1, text="2 días", font=("Poppins Bold", 14), text_color="#171717")
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

#------------------------------------------------------------------------------------------------------>
#boton_volver = CTkButton(master=master_app, image=returns_img, text="Volver", fg_color="#003b48", font=("Poppins Bold", 14), hover_color="#006278", anchor="w").pack(anchor="s", ipady=3, pady=(20, 20))
app.mainloop()
