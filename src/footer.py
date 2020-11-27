import tkinter as tk

from src.styles import *

class Footer(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.label_footer = tk.Label(parent, text="Powered by OpenWeatherMap",
            bg=COLOR_BLUE, font=(FONT, 12), anchor='s')
        self.label_footer.place(relx=0.5, rely=1, relwidth=1, height=20, anchor='s')

    def updateMode(self, darkTheme):
        self.label_footer['bg'] = COLOR_DARK_GRAY if darkTheme else COLOR_BLUE