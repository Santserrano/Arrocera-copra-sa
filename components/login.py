from customtkinter import *
from PIL import Image
from dashboard import dashboard
from CTkTable import CTkTable

def abrir_ventana_silos():
    app.withdraw()

    silos = CTkToplevel(app)
    silos.geometry("400x400")
    silos.title("Silos")

    CTkButton(master=silos, text="Silo 1").pack()
    CTkButton(master=silos, text="Silo 2").pack()
    CTkButton(master=silos, text="Silo 3").pack()

    volver = CTkButton(master=silos, text="Volver", command=lambda: [silos.destroy(), app.deiconify()])
    volver.pack()

app = CTk()
app.geometry("600x480")
app.resizable(0,0)

###########################################################################

# ref
side_image_label = None

def verificar():
    global side_image_label  # acceso ref

    for widget in frame.winfo_children():
        widget.destroy()

    if side_image_label:
        side_image_label.destroy()

    dashboard()

###########################################################################
side_img_data = Image.open("assets/side-img.png")
user_icon_data = Image.open("assets/user.png")
password_icon_data = Image.open("assets/password-icon.png")
google_icon_data = Image.open("assets/google-icon.png")

#
logo_img_data = Image.open("assets/logo.png")
analytics_img_data = Image.open("assets/analytics_icon.png")
package_img_data = Image.open("assets/package_icon.png")
list_img_data = Image.open("assets/list_icon.png")
returns_img_data = Image.open("assets/returns_icon.png")
settings_img_data = Image.open("assets/settings_icon.png")
person_img_data = Image.open("assets/person_icon.png")
logitics_img_data = Image.open("assets/gerente_icon.png")
shipping_img_data = Image.open("assets/factory_icon.png")
delivered_img_data = Image.open("assets/path_icon.png")
#


side_img = CTkImage(side_img_data, size=(300, 480))
user_icon = CTkImage(user_icon_data, size=(17,17))
password_icon = CTkImage(password_icon_data, size=(17,17))
google_icon = CTkImage(google_icon_data, size=(17,17))

# ref global
side_image_label = CTkLabel(master=app, text="", image=side_img)
side_image_label.pack(expand=True, side="left")

frame = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

CTkLabel(master=frame, text="Bienvenido", text_color="#003b48", anchor="w", justify="left", font=("Poppins Bold", 24)).pack(anchor="w", pady=(60, 1), padx=(25, 0))
CTkLabel(master=frame, text="Inicia sesión en tu cuenta", text_color="#7E7E7E", anchor="w", justify="left", font=("Poppins Light", 12)).pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Usuario:", text_color="#003b48", anchor="w", justify="left", font=("Poppins Bold", 12), image=user_icon, compound="left").pack(anchor="w", pady=(18, 0), padx=(25, 0))
CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#003b48", border_width=2, text_color="#000000").pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Contraseña:", text_color="#003b48", anchor="w", justify="left", font=("Poppins Bold", 12), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#003b48", border_width=2, text_color="#000000", show="*").pack(anchor="w", padx=(25, 0))

CTkButton(master=frame, text="Iniciar Sesión", fg_color="#003b48", hover_color="#00667d", font=("Poppins Bold", 12), text_color="#ffffff", width=225, command=verificar).pack(anchor="w", pady=(40, 0), padx=(25, 0))
CTkButton(master=frame, text="Continuar con Google", fg_color="#EEEEEE", hover_color="#EEEEEE", font=("Poppins Bold", 9), text_color="#003b48", width=225, image=google_icon).pack(anchor="w", pady=(20, 0), padx=(25, 0))

app.mainloop()
