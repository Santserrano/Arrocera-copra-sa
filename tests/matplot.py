import tkinter as tk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 2*x - 5

xs = np.arange(-5, 5, 0.25)
ys = f(xs)

def plot_graph():
    fig = plt.figure()
    plt.plot(xs, ys)
    plt.title('Gráfico de ejemplo')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    
    # Integrar la figura en Tkinter
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

window = tk.Tk()
window.title("Gráfico con Matplotlib")

plot_button = tk.Button(window, text="Trazar gráfico", command=plot_graph)
plot_button.pack()

window.mainloop()
