from customtkinter import *
from PIL import Image, ImageTk

def ventana_produccion(frame):
    app = CTk()
    app.geometry("856x645")
    app.resizable(0,0)

    set_appearance_mode("light")
    app.config(bg="#f5ecdd")