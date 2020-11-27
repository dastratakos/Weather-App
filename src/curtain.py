import tkinter as tk

from src.styles import *

class Curtain(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.label_home = tk.Label(parent, text="Enter a city...", fg=COLOR_LIGHT_GRAY,
            font=(FONT, 20), anchor='center')
        self.label_home.place(relwidth=1, relheight=1)

    def updateMode(self, darkTheme):
        # self.label_home['bg'] = COLOR_DARK_GRAY if darkTheme else COLOR_BLUE
        pass