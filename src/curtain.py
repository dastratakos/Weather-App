import tkinter as tk

from src.styles import *

class Curtain(tk.Frame):
    def __init__(self, parent, dark_mode):
        tk.Frame.__init__(self, parent)

        self.l_home = tk.Label(parent, text="Enter a city...", font=(FONT, 20),
            anchor='center')
        self.l_home.place(relwidth=1, relheight=1)

        self.updateMode(dark_mode)

    def updateMode(self, dark_mode):
        self.l_home['fg'] = COLOR_DARK_TEXT_TERTIARY if dark_mode else COLOR_TEXT_TERTIARY
        self.l_home['bg'] = COLOR_DARK_MAIN if dark_mode else COLOR_MAIN