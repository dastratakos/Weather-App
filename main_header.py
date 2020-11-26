from datetime import datetime

import tkinter as tk

from styles import *

class MainHeader(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.root = tk.Frame(parent)
        self.root.place(relx=0, rely=0, relwidth=1, relheight=0.2)

        self.label_location = tk.Label(self.root, fg=COLOR_GRAY,
            font=(FONT, 25), anchor='nw', justify='left')
        self.label_location.place(x=0, y=0, height=32)

        self.label_day = tk.Label(self.root, fg=COLOR_GRAY,
            font=(FONT, 15), anchor='nw', justify='left')
        self.label_day.place(x=0, y=32, height=20)

        self.label_condition = tk.Label(self.root, fg=COLOR_GRAY,
            font=(FONT, 15), anchor='nw', justify='left')
        self.label_condition.place(x=0, y=52, height=20)

    def format(self, current):
        self.label_day['text'] = datetime.fromtimestamp(current['dt']).strftime('%A')
        self.label_condition['text'] = current['weather'][0]['description'].capitalize()