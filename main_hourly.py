import tkinter as tk

from colors import *

class MainHourly(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.hourly_memory = []

        self.root = tk.Frame(parent, bg=COLOR_GRAY)
        self.root.place(relx=0, rely=0.475, relheight=0.275, relwidth=1)

        self.containers_hourly = []
        for i in range(8):
            self.containers_hourly.append({
                'frame': tk.Frame(self.root)
            })
            self.containers_hourly[-1]['frame'].place(relx=(0.125 * i), y=0, relwidth=0.125, relheight=1)

            self.containers_hourly[-1]['label'] = tk.Label(self.containers_hourly[-1]['frame'],
                fg=COLOR_LIGHT_GRAY, font=('Avenir Next', 15), anchor='n')
            self.containers_hourly[-1]['label'].place(relx=0, rely=0, relwidth=1, height=20)

            self.containers_hourly[-1]['stat'] = tk.Label(self.containers_hourly[-1]['frame'],
                font=('Avenir Next', 30))
            self.containers_hourly[-1]['stat'].place(relx=0, rely=0.5, relwidth=1, height=80, anchor='w')
    
    def formatHourly(self, mode):
        for i, hour_entry in enumerate(self.hourly_memory):
            self.containers_hourly[i]['stat']['text'] = hour_entry[mode]
            if mode == 'temp':
                self.containers_hourly[i]['stat']['font'] = ('Avenir Next', 30)
            if mode == 'humidity':
                self.containers_hourly[i]['stat']['font'] = ('Avenir Next', 25)
            if mode == 'wind':
                self.containers_hourly[i]['stat']['font'] = ('Avenir Next', 20)