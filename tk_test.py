import tkinter as tk
from tkinter import ttk

import numpy as np

from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from newton_raphson import nr_it
from gradient_descent import gd_it

from ast import literal_eval

from sympy import *

class Gui:
    def __init__(self):
        self.root = tk.Tk()
        
        self.label_func = ttk.Label(self.root, text='Funcao:')
        
        self.text_func = tk.Text(self.root, height=1)

        self.button_draw = ttk.Button(self.root, text='Draw!', command=self.draw)

        self.fig, self.ax = plt.subplots(subplot_kw={'projection': '3d'})
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)

        self.label_func.pack()
        self.text_func.pack()
        self.button_draw.pack()
        self.canvas.get_tk_widget().pack()

        self.root.mainloop()

    def draw(self):
        self.ax.clear()
        x, y = symbols('x y')
        f = eval(self.text_func.get('1.0', tk.END))
    
        lam_f = lambdify([x, y], f, modules=['numpy'])
    
        xv = np.arange(-10, +10, 0.5)
        yv = np.arange(-10, +10, 0.5)
        xv, yv = np.meshgrid(xv, yv)
        fv = lam_f(xv, yv)
    
        f_gr = self.ax.plot_surface(xv, yv, fv, cmap='winter')
        self.canvas.draw()

    def close(self):
        self.root.destroy()


if __name__ == '__main__':
    Gui()
