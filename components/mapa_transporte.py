import tkinter
import tkintermapview
from customtkinter import *
from PIL import Image, ImageTk
import os
# ventana

def mapa_transporte():

    def volver(root):
        from ID_log_2 import ID_log_2
        root.destroy()
        ID_log_2()

    root_tk = CTk()
    root_tk.geometry(f"{856}x{645}")
    root_tk.title("Transporte - Copra S.A")

    screen_width = root_tk.winfo_screenwidth()
    screen_height = root_tk.winfo_screenheight()
    window_width = 856
    window_height = 645
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2 - 50
    # Centro del escritorio
    root_tk.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

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
    frame.pack(expand=True, side="left", padx=3, pady=1)

    CTkLabel(master=frame, text="", image=logo_img).pack(pady=30, anchor="center")

    CTkComboBox(master=frame, width=160, values=["Ruta 1", "En proceso", "Enviado", "Entregado", "Pendiente", "Cancelado"], button_color="#003b48", border_color="#003b48", border_width=4, button_hover_color="#006278", dropdown_hover_color="#006278" , dropdown_fg_color="#003b48", dropdown_text_color="#fff").pack(side="top", padx=(10, 0), pady=10)
    CTkComboBox(master=frame, width=160, values=["Ruta 2", "En proceso", "Enviado", "Entregado", "Pendiente", "Cancelado"], button_color="#003b48", border_color="#003b48", border_width=4, button_hover_color="#006278", dropdown_hover_color="#006278" , dropdown_fg_color="#003b48", dropdown_text_color="#fff").pack(side="top", padx=(10, 0), pady=10)
    CTkComboBox(master=frame, width=160, values=["Ruta 3", "En proceso", "Enviado", "Entregado", "Pendiente", "Cancelado"], button_color="#003b48", border_color="#003b48", border_width=4, button_hover_color="#006278", dropdown_hover_color="#006278" , dropdown_fg_color="#003b48", dropdown_text_color="#fff").pack(side="top", padx=(10, 0), pady=10)
    CTkComboBox(master=frame, width=160, values=["Ruta 4", "En proceso", "Enviado", "Entregado", "Pendiente", "Cancelado"], button_color="#003b48", border_color="#003b48", border_width=4, button_hover_color="#006278", dropdown_hover_color="#006278" , dropdown_fg_color="#003b48", dropdown_text_color="#fff").pack(side="top", padx=(10, 0), pady=10)
    CTkComboBox(master=frame, width=160, values=["Ruta 5", "En proceso", "Enviado", "Entregado", "Pendiente", "Cancelado"], button_color="#003b48", border_color="#003b48", border_width=4, button_hover_color="#006278", dropdown_hover_color="#006278" , dropdown_fg_color="#003b48", dropdown_text_color="#fff").pack(side="top", padx=(10, 0), pady=10)
    CTkComboBox(master=frame, width=160, values=["Ruta 6", "En proceso", "Enviado", "Entregado", "Pendiente", "Cancelado"], button_color="#003b48", border_color="#003b48", border_width=4, button_hover_color="#006278", dropdown_hover_color="#006278" , dropdown_fg_color="#003b48", dropdown_text_color="#fff").pack(side="top", padx=(10, 0), pady=(10, 130))

    returns_img_data = Image.open("assets/returns_icon.png")
    returns_img = CTkImage(returns_img_data)
    CTkButton(master=frame, image=returns_img, command=lambda: volver(root_tk),text="Volver", fg_color="#003b48", font=("Poppins Bold", 14), hover_color="#006278", anchor="w").pack(anchor="center", ipady=3, pady=(20, 20))

    # Posición inicial y ajuste zoom
    map_widget.set_position(-30.95, -59.04, marker=False)
    map_widget.set_zoom(7.2)

    #-30.9514733 -59.0493214


    # Posición marcador
    marker_2 = map_widget.set_marker(-32.9434267, -60.6341945, text="Aduana Rosario")
    marker_3 = map_widget.set_marker(-29.18, -58.06, text="Copra S.A")#image=fabrica_image

    marker_4 = map_widget.set_marker(-31.0247433, -58.9335874, text="5h 58min", icon=camion_img_icon) ###
    marker_4 = map_widget.set_marker(-31.6540296, -60.6137915, text="6h 46min", icon=camion_img_icon) ###
    marker_4 = map_widget.set_marker(-29.6173030, -58.1239393, text="2h 24min", icon=camion_img_icon) ###

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

    #path_2 = map_widget.set_path([                                      (-32.907289749222166, -60.69293049456251), 
    #                                                                    (-32.89243707604069, -60.69700768158339),
    #                                                                    
    #                                                                    ], color="red", width=4)

    path_3 = map_widget.set_path([                                      (-32.9071580099362, -60.69262648382188), 
                                                                        (-32.894024641699474, -60.706653193310274),
                                                                        (-32.869769763467396, -60.72205979918642),
                                                                        (-32.83898210258531, -60.73999841316195),
                                                                        (-32.807534500060164, -60.74180085773984),
                                                                        (-32.75413465407075, -60.75647790518159),
                                                                        (-32.703086226549935, -60.78248460419761),
                                                                        (-32.6669664450752, -60.81398446642492),
                                                                        (-32.61818157304873, -60.8360429540348),
                                                                        (-32.55909823235539, -60.88307817088235),
                                                                        (-32.49541534736386, -60.900330139098266),
                                                                        (-32.42103747769254, -60.92865426671514),
                                                                        (-32.36044698065889, -60.95534761035777),
                                                                        (-32.26318541790707, -60.99097153001237),
                                                                        (-32.200894579926064, -60.9938925200534),
                                                                        (-32.09248405034989, -60.99638254072542),
                                                                        (-32.01610410683517, -60.99012714388655),
                                                                        (-31.978813401622414, -60.96994550129596),
                                                                        (-31.890707541660877, -60.90310294188715),
                                                                        (-31.809877395252535, -60.878636928409186),
                                                                        (-31.775761929801146, -60.84954830488532),
                                                                        (-31.73692826764018, -60.82997617665318),
                                                                        (-31.63187159258218, -60.776308791792644),
                                                                        (-31.623423522090167, -60.743499531548586),
                                                                        (-31.628511656427897, -60.7332395910599),
                                                                        (-31.64339045227513, -60.74214657236327),
                                                                        (-31.647709657016964, -60.74169558406252),
                                                                        (-31.66037816588932, -60.73380332214813),
                                                                        (-31.672565176813283, -60.72602380683254),
                                                                        (-31.665560239910988, -60.711592239661364),
                                                                        (-31.646557888738833, -60.70347448454944),
                                                                        (-31.640414883597188, -60.68430755997766),
                                                                        (-31.639071047124965, -60.63030193766741),
                                                                        (-31.65778702040956, -60.60797810808577),
                                                                        (-31.669398627069587, -60.581933642154034),
                                                                        (-31.68513435570141, -60.54145761142926),
                                                                        (-31.687149103953846, -60.53074668210436),
                                                                        (-31.68753286055782, -60.508535602145315),
                                                                        (-31.713720499147083, -60.501770805573),
                                                                        (-31.72638000204573, -60.502785524962),
                                                                        (-31.733006249504683, -60.487812964772274),
                                                                        (-31.729170493369182, -60.48161190183955),
                                                                        (-31.735115847693475, -60.45432722493556),
                                                                        (-31.748288205343602, -60.403009317973435),
                                                                        (-31.76411647842331, -60.39418322579568),
                                                                        (-31.744210710231666, -60.343810177333374),
                                                                        (-31.69568041422542, -60.250573687887574),
                                                                        (-31.612240213244874, -60.12383332400507),
                                                                        (-31.58500817021321, -60.070992928662854),
                                                                        (-31.58549743880314, -60.01145176498265),
                                                                        (-31.565909218646052, -59.95792088016508),
                                                                        (-31.576947572753138, -59.87463234305151),
                                                                        (-31.56551496743745, -59.8117032226633),
                                                                        (-31.520164975758732, -59.65530584026853),
                                                                        (-31.366995644101085, -59.39063336870727),
                                                                        (-31.288735517241797, -59.2610734091269),
                                                                    
                                                                        ], color="red", width=4)


    #funciones que quizás sirvan
    # path_1.add_position(...)
    # path_1.remove_position(...)
    # path_1.delete()
    # marker_3.set_position(...)
    # marker_3.set_text(...)
    # marker_3.delete()

    root_tk.mainloop()
