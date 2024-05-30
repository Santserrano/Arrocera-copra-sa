import tkinter
import tkintermapview

# ventana
root_tk = tkinter.Tk()
root_tk.geometry(f"{856}x{645}")
root_tk.title("Transporte - Copra S.A")

#856x645

# Crear widget mapa
map_widget = tkintermapview.TkinterMapView(root_tk, width=856, height=645, corner_radius=0)
map_widget.pack(fill="both", expand=True)

# Posición inicial y ajuste zoom
map_widget.set_position(-30.95, -59.04, marker=False)
map_widget.set_zoom(7)

#-30.9514733 -59.0493214


# Posición marcador
marker_2 = map_widget.set_marker(-32.94, -60.63, text="Aduana Rosario")
marker_3 = map_widget.set_marker(-29.18, -58.06, text="Copra S.A")


# trazo         Aduana: -32.9437122 -60.6348338     Copra S.A: -29.1834803 -58.0666058
path_1 = map_widget.set_path([marker_2.position, marker_3.position, (-32.94, -60.63), 
                                                                    (-29.18, -58.06)])

#funciones que quizás sirvan
# path_1.add_position(...)
# path_1.remove_position(...)
# path_1.delete()
# marker_3.set_position(...)
# marker_3.set_text(...)
# marker_3.delete()

root_tk.mainloop()
