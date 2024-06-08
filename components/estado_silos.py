import tkinter
import tkintermapview
from customtkinter import *
from PIL import Image, ImageTk
import os

# ventana
app = tkinter.Tk()
app.geometry(f"{856}x{645}")
app.title("Estado Silos - Copra S.A")

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
window_width = 856
window_height = 645
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2 - 50
# Centro del escritorio
app.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")


logo_img_data = Image.open("assets/logo.png")
###################################################################################################
border_frame = CTkFrame(master=app, fg_color="#003b48", width=856, height=645)
border_frame.pack_propagate(0)
border_frame.pack(expand=True)

logo_img = CTkImage(logo_img_data, size=(90, 100))

cards_frame = CTkFrame(master=border_frame, width=400, height=400)
cards_frame.place(relx=0.5, rely=0.5)

# Crear las cuatro tarjetas
for i in range(2):
    for j in range(2):
        card = CTkFrame(master=cards_frame, width=200, height=200, fg_color="#ffffff")
        card.grid(row=i, column=j, padx=10, pady=10)
        
        # Agregar contenido a cada tarjeta (opcional)
        label = CTkLabel(master=card, text=f"Tarjeta {i*2 + j + 1}")
        label.place(relx=0.5, rely=0.5)


app.mainloop()
