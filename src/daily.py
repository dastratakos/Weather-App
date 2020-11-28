import tkinter as tk

from src.styles import *
from src.day    import Day

NUM_DAYS = 8
class Daily(tk.Frame):
    def __init__(self, parent, dark_mode):
        tk.Frame.__init__(self, parent)

        self.root = tk.Frame(parent)
        self.root.place(relx=0, rely=0.75, relwidth=1, relheight=0.25)

        self.days = []
        for i in range(NUM_DAYS):
            self.days.append(Day(self.root, i, dark_mode))

        self.updateMode(dark_mode)
    
    def format(self, res):
        """
        Args:
            res (dict): sub-response that contains daily information
        """
        for i in range(NUM_DAYS):
            self.days[i].format(res[i])

    def updateMode(self, dark_mode):
        self.root['bg'] = COLOR_DARK_MAIN if dark_mode else COLOR_MAIN
        for i in range(NUM_DAYS):
            self.days[i].updateMode(dark_mode)