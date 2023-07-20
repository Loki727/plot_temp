import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from graphFunctions import *


def main():
    x=[]

    r=tk.Tk()
    fig, ax = plt.subplots()
    ax.set_ylim(-40, 40)
    ax.set_xlim(0, 20)
    ax.set_xticks(np.arange(1, 20))
    ax.grid()
    r.title("App")
    r.geometry("800x600")
    
    canvas = FigureCanvasTkAgg(fig, master=r)
    canvas.get_tk_widget().pack()


    framePlot= tk.Frame(r)
    titleText= tk.Label(text="Plot, testing")
    titleText.config(font=("Courier", 27))
    titleText.pack()
    framePlot.pack()

    tk.Button(framePlot, text="push random data", command=lambda:graph_random_data(x, ax, canvas)).pack(pady=10, side="left")
    tk.Button(framePlot, text="push api data", command=lambda:graph_openweathermap(x, ax, canvas)).pack(side="left")
    tk.Button(framePlot, text="push database data", command=lambda:graph_random_data(x, ax, canvas)).pack(side="left")
    
    r.mainloop()

if __name__ == "__main__":
    main()

