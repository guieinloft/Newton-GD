import tkinter as tk
from tkinter import ttk

import numpy as np

from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from newton_raphson import nr_it

from ast import literal_eval

from sympy import *

class NewtonGUI:
    def __init__(self):
        self.root = tk.Tk()
        
        self.f = ''
        self.label_f = ttk.Label(self.root, text='Função f:')
        self.text_f = tk.Text(self.root, height=1)

        self.g = ''
        self.label_g = ttk.Label(self.root, text='Função g:')
        self.text_g = tk.Text(self.root, height=1)

        self.x0 = 0.0
        self.y0 = 0.0
        self.x1 = 0.0
        self.y1 = 0.0
        self.label_p = ttk.Label(self.root, text='Ponto P(x0, y0):')
        self.text_p = tk.Text(self.root, height=1)

        self.err = 2
        self.label_err = ttk.Label(self.root, text='Erro (em casas decimais):')
        self.i = 0
        self.text_err = tk.Text(self.root, height=1)

        self.button_at = ttk.Button(self.root, text='Atualizar', command=self.update)

        self.button_next = ttk.Button(self.root, text='Próxima iteração', command=self.next_it)

        self.button_solve = ttk.Button(self.root, text='Resolver', command=self.solve)

        self.fig, self.ax = plt.subplots(subplot_kw={'projection': '3d'})
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)

        self.str_p1 = '' 
        self.label_p1 = ttk.Label(self.root, text=self.str_p1)

        self.label_f.pack()
        self.text_f.pack()
        self.label_g.pack()
        self.text_g.pack()
        self.label_p.pack()
        self.text_p.pack()
        self.label_err.pack()
        self.text_err.pack()
        self.button_at.pack()
        self.canvas.get_tk_widget().pack()
        self.label_p1.pack()
        self.button_next.pack()
        self.button_solve.pack()

        self.root.mainloop()


    def draw(self):
        x, y = symbols('x y')
        lam_f = lambdify([x, y], self.f, modules=['numpy'])
        lam_g = lambdify([x, y], self.g, modules=['numpy'])

        f0 = lam_f(self.x1, self.y1)
        g0 = lam_g(self.x1, self.y1)
        
        xv = np.arange(float(self.x1-1), float(self.x1+1), 0.1)
        yv = np.arange(float(self.y1-1), float(self.y1+1), 0.1)
        xv, yv = np.meshgrid(xv, yv)
        fv = lam_f(xv, yv)
        gv = lam_g(xv, yv)

        self.ax.clear()
        f_gr = self.ax.plot_surface(xv, yv, fv, cmap='winter')
        g_gr = self.ax.plot_surface(xv, yv, gv, cmap='autumn')
        fp_gr = self.ax.plot([self.x1], [self.y1], [f0], markerfacecolor='g', markeredgecolor='g', marker='o', markersize=5, alpha=0.5, zorder=100)
        gp_gr = self.ax.plot([self.x1], [self.y1], [g0], markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5, alpha=0.5, zorder=100)
        self.canvas.draw()


    def update(self):
        x, y = symbols('x y')
        self.i = 0
        try:
            self.f = eval(self.text_f.get('1.0', tk.END))
            self.g = eval(self.text_g.get('1.0', tk.END))
            self.x0, self.y0 = literal_eval(self.text_p.get('1.0', tk.END))
            self.x1 = self.x0
            self.y1 = self.y0
            self.err = int(self.text_err.get('1.0', tk.END))

            self.draw()
            self.str_p1 = '%d: %.' + str(self.err) + 'f, %.' + str(self.err) + 'f' 
            self.label_p1['text'] = (self.str_p1 % (self.i, self.x1, self.y1))
        except:
            tk.messagebox.showinfo(title='Erro', message='Uma ou mais informações não foram preenchidas corretamente.')
        

    def next_it(self):
        self.i = self.i + 1
        self.x0 = self.x1
        self.y0 = self.y1

        self.x1, self.y1 = nr_it(self.x0, self.y0, self.f, self.g)
        self.draw()
        self.label_p1['text'] = (self.str_p1 % (self.i, self.x1, self.y1))


    def solve(self):
        self.i = 1
        self.x1, self.y1 = nr_it(self.x0, self.y0, self.f, self.g)
        while round(self.x0, self.err) != round(self.x1, self.err) or round(self.y0, self.err) != round(self.y1, self.err):
            self.i = self.i + 1
            self.x0 = self.x1
            self.y0 = self.y1
            self.x1, self.y1 = nr_it(self.x0, self.y0, self.f, self.g)
        
        self.draw()
        self.label_p1['text'] = (self.str_p1 % (self.i, self.x1, self.y1))


if __name__ == '__main__':
    NewtonGUI()
