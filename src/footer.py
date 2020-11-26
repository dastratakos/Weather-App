import tkinter as tk

from src.styles import *

class Footer(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)

        self.label_footer = tk.Label(root, text="Powered by OpenWeatherMap",
            bg=COLOR_BLUE, font=(FONT, 12), anchor='s')
        self.label_footer.place(relx=0.5, rely=1, relwidth=1, height=20, anchor='s')