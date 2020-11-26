import tkinter as tk

from styles import *

class Curtain(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.root = tk.Frame(parent, bd=10)
        self.root.place(relx=0, rely=0, relwidth=1, relheight=1)

        label_home = tk.Label(self.root, text="Enter a city...", fg=COLOR_LIGHT_GRAY,
            font=(FONT, 20), anchor='center')
        label_home.place(relwidth=1, relheight=1)