import tkinter as tk
from tkinter import ttk

from newton_gui import NewtonGUI
from gradient_gui import GradientGUI

class MenuGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.button_nr = ttk.Button(self.root, text='Método de Newton', command=self.nr_window)
        self.button_gd = ttk.Button(self.root, text='Descida de Gradiente', command=self.gd_window)

        self.button_nr.pack()
        self.button_gd.pack()

        self.root.protocol('WM_DELETE_WINDOW', self.close)

        self.root.mainloop()

    def nr_window(self):
        NewtonGUI()


    def gd_window(self):
        GradientGUI()


    def close(self):
        exit()


if __name__ == '__main__':
    MenuGUI()
