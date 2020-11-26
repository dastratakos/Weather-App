import tkinter as tk

from src.styles import *
from src.hour   import Hour

NUM_HOURS = 8

class Hourly(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.root = tk.Frame(parent, bg=COLOR_GRAY)
        self.root.place(relx=0, rely=0.475, relheight=0.275, relwidth=1)

        self.hours = []
        for i in range(NUM_HOURS):
            self.hours.append(Hour(self.root, i))

    def format(self, res):
        for i in range(NUM_HOURS):
            self.hours[i].format(res[i])
            self.hours[i].showStat('temp')
    
    def showStat(self, stat):
        for i in range(NUM_HOURS):
            self.hours[i].showStat(stat)