from customtkinter import *
from CTkTable import CTkTable
from PIL import Image

def dashboard():
    app = CTk()
    app.geometry("856x645")
    app.resizable(0,0)

    app.iconbitmap('assets/logo.png') #Debe ser formato .ico :/
    app.title("Agrorice - Copra S.A")

    set_appearance_mode("light")

    sidebar_frame = CTkFrame(master=app, fg_color="#003b48",  width=176, height=650, corner_radius=0)
    sidebar_frame.pack_propagate(0)
    sidebar_frame.pack(fill="y", anchor="w", side="left")

    logo_img_data = Image.open("assets/logo.png")
    logo_img = CTkImage(logo_img_data, size=(90, 100))

    CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")

    analytics_img_data = Image.open("assets/analytics_icon.png")
    analytics_img = CTkImage(analytics_img_data)

    CTkButton(master=sidebar_frame, image=analytics_img, text="Panel Principal", fg_color="transparent", font=("Poppins Bold", 14), hover_color="#006278", anchor="w").pack(anchor="center", ipady=5, pady=(60, 0))

    package_img_data = Image.open("assets/package_icon.png")
    package_img = CTkImage(package_img_data)

    CTkButton(master=sidebar_frame, image=package_img, text="Nuevos", fg_color="#fff", font=("Poppins Bold", 14), text_color="#003b48", hover_color="#006278", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))
        #########################################################################################################


    list_img_data = Image.open("assets/list_icon.png")
    list_img = CTkImage(list_img_data)
    CTkButton(master=sidebar_frame, image=list_img, text="Ordenes", fg_color="transparent", font=("Poppins Bold", 14), hover_color="#006278", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))


        #########################################################################################################
    returns_img_data = Image.open("assets/returns_icon.png")
    returns_img = CTkImage(returns_img_data)
    CTkButton(master=sidebar_frame, image=returns_img, text="Actualizar", fg_color="transparent", font=("Poppins Bold", 14), hover_color="#006278", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

    settings_img_data = Image.open("assets/settings_icon.png")
    settings_img = CTkImage(settings_img_data)
    CTkButton(master=sidebar_frame, image=settings_img, text="Configuración", fg_color="transparent", font=("Poppins Bold", 14), hover_color="#006278", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

    person_img_data = Image.open("assets/person_icon.png")
    person_img = CTkImage(person_img_data)
    CTkButton(master=sidebar_frame, image=person_img, text="Cuenta", fg_color="transparent", font=("Poppins Bold", 14), hover_color="#006278", anchor="w").pack(anchor="center", ipady=5, pady=(160, 0))

    main_view = CTkFrame(master=app, fg_color="#fff",  width=680, height=650, corner_radius=0)
    main_view.pack_propagate(0)
    main_view.pack(side="left")

    title_frame = CTkFrame(master=main_view, fg_color="transparent")
    title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

    CTkLabel(master=title_frame, text="Menú principal", font=("Poppins Bold", 25), text_color="#003b48").pack(anchor="nw", side="left")

    CTkButton(master=title_frame, text="+ Nueva Orden",  font=("Poppins Bold", 15), text_color="#fff", fg_color="#003b48", hover_color="#006278").pack(anchor="ne", side="right")

    metrics_frame = CTkFrame(master=main_view, fg_color="transparent")
    metrics_frame.pack(anchor="n", fill="x",  padx=27, pady=(36, 0))

    orders_metric = CTkFrame(master=metrics_frame, fg_color="#003b48", width=200, height=60)
    orders_metric.grid_propagate(0)
    orders_metric.pack(side="left")

    logitics_img_data = Image.open("assets/gerente_icon.png")
    logistics_img = CTkImage(logitics_img_data, size=(43, 43))

    CTkLabel(master=orders_metric, image=logistics_img, text="").grid(row=0, column=0, rowspan=2, padx=(12,5), pady=10)

    CTkLabel(master=orders_metric, text="Ordenes", text_color="#fff", font=("Poppins Bold", 15)).grid(row=0, column=1, sticky="sw")
    CTkLabel(master=orders_metric, text="123", text_color="#fff",font=("Poppins Bold", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0,10))


    shipped_metric = CTkFrame(master=metrics_frame, fg_color="#003b48", width=200, height=60)
    shipped_metric.grid_propagate(0)
    shipped_metric.pack(side="left",expand=True, anchor="center")

    shipping_img_data = Image.open("assets/factory_icon.png")
    shipping_img = CTkImage(shipping_img_data, size=(43, 43))

    CTkLabel(master=shipped_metric, image=shipping_img, text="").grid(row=0, column=0, rowspan=2, padx=(12,5), pady=10)

    CTkLabel(master=shipped_metric, text="Pendientes", text_color="#fff", font=("Poppins Bold", 15)).grid(row=0, column=1, sticky="sw")
    CTkLabel(master=shipped_metric, text="91", text_color="#fff",font=("Poppins Bold", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0,10))

    delivered_metric = CTkFrame(master=metrics_frame, fg_color="#003b48", width=200, height=60)
    delivered_metric.grid_propagate(0)
    delivered_metric.pack(side="right",)

    delivered_img_data = Image.open("assets/path_icon.png")
    delivered_img = CTkImage(delivered_img_data, size=(43, 43))

    CTkLabel(master=delivered_metric, image=delivered_img, text="").grid(row=0, column=0, rowspan=2, padx=(12,5), pady=10)

    CTkLabel(master=delivered_metric, text="Enviados", text_color="#fff", font=("Poppins Bold", 15)).grid(row=0, column=1, sticky="sw")
    CTkLabel(master=delivered_metric, text="23", text_color="#fff",font=("Poppins Bold", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0,10))

    search_container = CTkFrame(master=main_view, height=50, fg_color="#F0F0F0")
    search_container.pack(fill="x", pady=(45, 0), padx=27)

    CTkEntry(master=search_container, width=305, placeholder_text="Buscar orden", border_color="#003b48", border_width=2).pack(side="left", padx=(13, 0), pady=15)

    CTkComboBox(master=search_container, width=125, values=["Fecha", "Más reciente", "Últimas entregas"], button_color="#003b48", border_color="#003b48", border_width=2, button_hover_color="#006278",dropdown_hover_color="#006278" , dropdown_fg_color="#003b48", dropdown_text_color="#fff").pack(side="left", padx=(13, 0), pady=15)
    CTkComboBox(master=search_container, width=125, values=["Estado", "En proceso", "Enviado", "Entregado", "Pendiente", "Cancelado"], button_color="#003b48", border_color="#003b48", border_width=2, button_hover_color="#006278",dropdown_hover_color="#006278" , dropdown_fg_color="#003b48", dropdown_text_color="#fff").pack(side="left", padx=(13, 0), pady=15)

    table_data = [
        ["N° Orden", "Item", "Cliente", "Dirección", "Estado", "Cantidad"],
        ['3833', 'Arroz blanco', 'Juan Perez', 'Av. Rivadavia 123', 'Enviado', '8'],
        ['6432', 'Arroz integral', 'María Gomez', 'Calle Corrientes 456', 'Entregado', '10'],
        ['2180', 'Arroz blanco', 'Pedro Rodriguez', 'Av. Belgrano', 'Pendiente', '3']
    ]

    table_frame = CTkScrollableFrame(master=main_view, fg_color="transparent")
    table_frame.pack(expand=True, fill="both", padx=27, pady=21)
    table = CTkTable(master=table_frame, values=table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#003b48", hover_color="#d5eae8")
    table.edit_row(0, text_color="#fff", hover_color="#006278")
    table.pack(expand=True)

    app.mainloop()

if __name__ == "__main__":
    dashboard()