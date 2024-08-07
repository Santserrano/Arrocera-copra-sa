import tkinter as tk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 2*x - 5

xs = np.arange(-5, 5, 0.25)
ys = f(xs)

meses = np.arange(1, 13)
ventas = np.random.randint(10, 50, size=12)

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

def plot_graph2():

    meses = np.arange(1, 13)
    ventas = np.random.randint(10, 50, size=12)

    fig = plt.figure(figsize=(10, 6))
    plt.bar(meses, ventas, color='blue')

    plt.xlabel('Mes')
    plt.ylabel('Ventas ($)')
    plt.title('Simulación de Ventas Mensuales')

    plt.xticks(meses)
    plt.grid(True)
    
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

window = tk.Tk()
window.title("Gráfico con Matplotlib")

plot_button = tk.Button(window, text="Trazar gráfico", command=plot_graph2)
plot_button.pack()


window.mainloop()
