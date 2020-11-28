import tkinter as tk

from src.styles import *

class Footer(tk.Frame):
    def __init__(self, parent, dark_mode):
        tk.Frame.__init__(self, parent)

        self.l_footer = tk.Label(parent, text="Powered by OpenWeatherMap",
            font=(FONT, 12), anchor='s')
        self.l_footer.place(relx=0.5, rely=1, relwidth=1, height=20, anchor='s')

        self.updateMode(dark_mode)

    def updateMode(self, dark_mode):
        self.l_footer['fg'] = COLOR_DARK_TEXT_TERTIARY if dark_mode else COLOR_TEXT_TERTIARY
        self.l_footer['bg'] = COLOR_DARK_MAIN if dark_mode else COLOR_MAIN