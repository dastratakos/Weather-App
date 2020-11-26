import tkinter as tk

from colors import *

class Curtain(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.root = tk.Frame(parent, bd=10)
        self.root.place(relx=0.5, rely=0.95, relwidth=0.85, relheight=0.65, anchor='s')

        label_home = tk.Label(self.root, text="Enter a city...", fg=COLOR_LIGHT_GRAY,
            font=('Avenir Next', 20), anchor='center')
        label_home.place(relwidth=1, relheight=1)