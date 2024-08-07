from customtkinter import *
from PIL import Image
from CTkTable import CTkTable
import tkinter as tk
import sqlite3

#--------------------------------------------------------------------------------------------#

def login():
    def iniciar_sesion(usuario, password, app):
        conn = sqlite3.connect('usuarios.db')
        c = conn.cursor()
        c.execute("SELECT rol FROM usuarios WHERE usuario=? AND password=?", (usuario, password))
        result = c.fetchone()
        
        if result:
            rol = result[0]
            app.destroy()  # Cierra la ventana de inicio de sesión
            ventanas(rol)
        else:
            print("Login Failed")
        
        conn.close()

    def ventanas(rol):
        if rol == 'Gerente_general':
            from ID_log import ID_log
            ID_log()
        elif rol == 'Gerente_transporte':
            from ID_log_2 import ID_log_2
            ID_log_2()
        elif rol == 'Gerente_producción':
            from dashboard import dashboard
            dashboard()

    app = CTk()
    app.geometry("600x480")
    app.resizable(0,0)

    # Centro del escritorio
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    window_width = 600
    window_height = 480
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2 - 50
    app.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    ###########################################################################
    side_img_data = Image.open("assets/side-img.png")
    user_icon_data = Image.open("assets/user.png")
    password_icon_data = Image.open("assets/password-icon.png")
    google_icon_data = Image.open("assets/google-icon.png")

    side_img = CTkImage(side_img_data, size=(300, 480))
    user_icon = CTkImage(user_icon_data, size=(17,17))
    password_icon = CTkImage(password_icon_data, size=(17,17))
    google_icon = CTkImage(google_icon_data, size=(17,17))

    # ref global
    side_image_label = CTkLabel(master=app, text="", image=side_img)
    side_image_label.pack(expand=True, side="left")

    frame = CTkFrame(master=app, width=300, height=480, fg_color="#fff")
    frame.pack_propagate(0)
    frame.pack(expand=True, side="right")

    CTkLabel(master=frame, text="Bienvenido", text_color="#003b48", anchor="w", justify="left", font=("Poppins Bold", 24)).pack(anchor="w", pady=(60, 1), padx=(25, 0))
    CTkLabel(master=frame, text="Inicia sesión en tu cuenta", text_color="#7E7E7E", anchor="w", justify="left", font=("Poppins Light", 12)).pack(anchor="w", padx=(25, 0))

    CTkLabel(master=frame, text="  Usuario:", text_color="#003b48", anchor="w", justify="left", font=("Poppins Bold", 12), image=user_icon, compound="left").pack(anchor="w", pady=(18, 0), padx=(25, 0))
    username_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#003b48", border_width=2, text_color="#000000")
    username_entry.pack(anchor="w", padx=(25, 0))

    CTkLabel(master=frame, text="  Contraseña:", text_color="#003b48", anchor="w", justify="left", font=("Poppins Bold", 12), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
    password_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#003b48", border_width=2, text_color="#000000", show="*")
    password_entry.pack(anchor="w", padx=(25, 0))

    CTkButton(master=frame, text="Iniciar Sesión", command=lambda: iniciar_sesion(username_entry.get(), password_entry.get(), app), fg_color="#003b48", hover_color="#00667d", font=("Poppins Bold", 12), text_color="#fff", width=225).pack(anchor="w", pady=(40, 0), padx=(25, 0))
    CTkButton(master=frame, text="Continuar con Google", fg_color="#EEEEEE", hover_color="#EEEEEE", font=("Poppins Bold", 9), text_color="#003b48", width=225, image=google_icon).pack(anchor="w", pady=(20, 0), padx=(25, 0))

    app.mainloop()

if __name__ == "__main__":
    login()
