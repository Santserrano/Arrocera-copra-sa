import tkinter
import tkintermapview
from customtkinter import *
from PIL import Image, ImageTk
import os
# ventana
root_tk = tkinter.Tk()
root_tk.geometry(f"{856}x{645}")
root_tk.title("Transporte - Copra S.A")

#856x645

# Crear widget mapa
map_widget = tkintermapview.TkinterMapView(root_tk, width=656, height=645, corner_radius=0)
map_widget.pack(fill="both", expand=True, side="right")

logo_img_data = Image.open("assets/logo.png")
copra_img_data = Image.open("assets/copra-sa.jpg")
camion_icon_image = Image.open("assets/icon-camion.png")
###################################################################################################
border_frame = CTkFrame(master=root_tk, fg_color="#003b48", width=204, height=649)
border_frame.pack_propagate(0)
border_frame.pack(expand=True, side="left")

logo_img = CTkImage(logo_img_data, size=(90, 100))
fabrica_image = CTkImage(copra_img_data, size=(100, 70)) #####
camion_img_icon = ImageTk.PhotoImage(Image.open("assets/icon-camion.png").resize((35, 35)))

frame = CTkFrame(master=border_frame, width=198, height=643, fg_color="#f5ecdd")
frame.pack_propagate(0)
frame.pack(expand=True, side="left", padx=3, pady=3)

CTkLabel(master=frame, text="", image=logo_img).pack(pady=50, anchor="center")

CTkComboBox(master=frame, width=160, values=["Ruta 1", "En proceso", "Enviado", "Entregado", "Pendiente", "Cancelado"], button_color="#003b48", border_color="#003b48", border_width=4, button_hover_color="#006278", dropdown_hover_color="#006278" , dropdown_fg_color="#003b48", dropdown_text_color="#fff").pack(side="top", padx=(10, 0), pady=30)
CTkComboBox(master=frame, width=160, values=["Ruta 2", "En proceso", "Enviado", "Entregado", "Pendiente", "Cancelado"], button_color="#003b48", border_color="#003b48", border_width=4, button_hover_color="#006278", dropdown_hover_color="#006278" , dropdown_fg_color="#003b48", dropdown_text_color="#fff").pack(side="top", padx=(10, 0), pady=30)
CTkComboBox(master=frame, width=160, values=["Ruta 3", "En proceso", "Enviado", "Entregado", "Pendiente", "Cancelado"], button_color="#003b48", border_color="#003b48", border_width=4, button_hover_color="#006278", dropdown_hover_color="#006278" , dropdown_fg_color="#003b48", dropdown_text_color="#fff").pack(side="top", padx=(10, 0), pady=30)
# Posición inicial y ajuste zoom
map_widget.set_position(-30.95, -59.04, marker=False)
map_widget.set_zoom(7.2)

#-30.9514733 -59.0493214


# Posición marcador
marker_2 = map_widget.set_marker(-32.9434267, -60.6341945, text="Aduana Rosario")
marker_3 = map_widget.set_marker(-29.18, -58.06, text="Copra S.A")#image=fabrica_image

marker_4 = map_widget.set_marker(-31.1617608, -59.1388770, text="6h 46min", icon=camion_img_icon) ###

# trazo         Aduana: -32.9437122 -60.6348338     Copra S.A: -29.1834803 -58.0666058

path_1 = map_widget.set_path([                                      (-32.9434267, -60.6341945), 
                                                                    (-32.94294533928551, -60.63412434689571),
                                                                    (-32.9415495964004, -60.63475519487584),
                                                                    (-32.939688571615946, -60.6365521557889),
                                                                    (-32.93769915691722, -60.63894173180363),
                                                                    (-32.93535672425774, -60.643434134086306),
                                                                    (-32.93092839429363, -60.649608798314205),
                                                                    (-32.92722190425361, -60.65773335603583),
                                                                    (-32.9245422238164, -60.66293307310231),
                                                                    (-32.92189455566289, -60.66786515772977),
                                                                    (-32.92218339601417, -60.68524215279491),
                                                                    (-32.91998497608799, -60.68837727665748),
                                                                    (-32.91611755017183, -60.690690386110184),
                                                                    (-32.91109445839235, -60.692315297850506),
                                                                    (-32.90727479205206, -60.693309361463854),
                                                                    (-32.907916764297795, -60.713936179713244),
                                                                    (-32.90823774866967, -60.72274893582685),
                                                                    (-32.905990833642214, -60.72393416536524),
                                                                    (-32.895477723573414, -60.72133430689742),
                                                                    (-32.89167343587561, -60.718103600484184),
                                                                    (-32.87623277619924, -60.70566851562114),
                                                                    (-32.87220288245043, -60.69878653719688),
                                                                    (-32.87011561447306, -60.68542402932469),
                                                                    (-32.8619731080096, -60.627120910548726),
                                                                    (-32.80463242481569, -60.50960648887947),
                                                                    (-32.76736293788411, -60.43479001729881),
                                                                    (-32.67496732437542, -60.27176428059364),
                                                                    (-32.645744464691035, -60.21529521243517),
                                                                    (-32.59300055198652, -60.158236868485176),
                                                                    (-32.608800211654234, -60.116118589685506),
                                                                    (-32.42369845717681, -59.825595211574736),
                                                                    (-32.39136019419488, -59.79380783308404),
                                                                    (-32.39498372922743, -59.74946443920712),
                                                                    (-32.41120020085617, -59.5607196418471),
                                                                    (-32.4081140492391, -59.52209797414657),
                                                                    (-32.382615717871346, -59.49094634472693),
                                                                    (-32.36785023498135, -59.34742632763412),
                                                                    (-32.35227674904894, -59.3088046599003),
                                                                    (-32.2759816677355, -59.27383854460177),
                                                                    (-32.17635229785439, -59.27781196669943),
                                                                    (-32.053447055179625, -59.256514422927054),
                                                                    (-31.9706992818957, -59.21693913597139),
                                                                    (-31.849407873058393, -59.17974790246524),
                                                                    (-31.817925446825285, -59.171106798673065),
                                                                    (-31.763077616820887, -59.18986135107877),
                                                                    (-31.666677479281073, -59.17253723183507),
                                                                    (-31.5351509775507, -59.21316924602337),
                                                                    (-31.349445369488475, -59.23617187019938),
                                                                    (-31.287852985714242, -59.26037612490128),
                                                                    (-31.10712719183326, -59.08046066039571),
                                                                    (-31.02963612868658, -58.944732564250444),
                                                                    (-30.94863204536991, -58.78285760820807),
                                                                    (-30.735722530352778, -58.59098002747403),
                                                                    (-30.68672389635699, -58.56935069354632),
                                                                    (-30.53316073114049, -58.43477992751322),
                                                                    (-30.348825872208238, -58.32132234764211),
                                                                    (-30.082752804753056, -58.02938305615922),
                                                                    (-30.07619576611403, -58.003373829318136),
                                                                    (-29.811040301700885, -58.08837148168507),
                                                                    (-29.714922194494324, -58.07529163343097),
                                                                    (-29.544459500919732, -58.17754040076599),
                                                                    (-29.425685380243518, -58.20137791372352),
                                                                    (-29.221953666716853, -58.11782070719806),
                                                                    (-29.179048625547175, -58.10840004235797),
                                                                    (-29.18459153606841, -58.07522291706866),
                                                                    (-29.18369753843127, -58.06723583166076),
                                                                    ], color="green", width=4)


#funciones que quizás sirvan
# path_1.add_position(...)
# path_1.remove_position(...)
# path_1.delete()
# marker_3.set_position(...)
# marker_3.set_text(...)
# marker_3.delete()

root_tk.mainloop()
