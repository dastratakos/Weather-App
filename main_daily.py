import tkinter as tk

from colors import *

class MainDaily(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.root = tk.Frame(parent)
        self.root.place(relx=0, rely=0.75, relwidth=1, relheight=0.25)

        self.containers_daily = []
        for i in range(8):
            self.containers_daily.append({
                'frame': tk.Frame(self.root)
            })
            self.containers_daily[-1]['frame'].place(relx=(0.125 * i), y=0, relwidth=0.125, relheight=1)

            self.containers_daily[-1]['label'] = tk.Label(self.containers_daily[-1]['frame'],
                fg=COLOR_LIGHT_GRAY, font=('Avenir Next', 15), anchor='n')
            self.containers_daily[-1]['label'].place(relx=0, rely=0, relwidth=1, height=20)

            self.containers_daily[-1]['icon'] = tk.Canvas(self.containers_daily[-1]['frame'],
                bd=0, highlightthickness=0)
            self.containers_daily[-1]['icon'].place(relx=0, rely=0.5, relwidth=1, height=60, anchor='w')

            self.containers_daily[-1]['temp'] = tk.Label(self.containers_daily[-1]['frame'],
                font=('Avenir Next', 15), anchor='n')
            self.containers_daily[-1]['temp'].place(relx=0.5, rely=1, relwidth=1, height=20, anchor='s')