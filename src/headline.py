from datetime import datetime

import tkinter as tk

from src.styles import *

class Headline(tk.Frame):
    def __init__(self, parent, dark_mode):
        tk.Frame.__init__(self, parent)

        self.root = tk.Frame(parent)
        self.root.place(relx=0, rely=0, relwidth=1, relheight=0.2)

        self.l_location = tk.Label(self.root, font=(FONT, 25), anchor='nw')
        self.l_location.place(x=0, y=0, height=32)

        self.l_day = tk.Label(self.root, font=(FONT, 15), anchor='nw')
        self.l_day.place(x=0, y=32, height=20)

        self.l_condition = tk.Label(self.root, font=(FONT, 15), anchor='nw')
        self.l_condition.place(x=0, y=52, height=20)

        self.updateMode(dark_mode)

    def format(self, city, current):
        self.l_location['text'] = city['name'] + \
            (f", {city['state']}" if city['state'] else '') + \
            (f", {city['country']}" if city['country'] else '')
        self.l_day['text'] = datetime.fromtimestamp(current['dt']).strftime('%A')
        self.l_condition['text'] = current['weather'][0]['description'].capitalize()

    def updateMode(self, dark_mode):
        self.root['bg'] = COLOR_DARK_MAIN if dark_mode else COLOR_MAIN
        for element in [self.l_location, self.l_day, self.l_condition]:
            element['fg'] = COLOR_DARK_TEXT_TERTIARY if dark_mode else COLOR_TEXT_TERTIARY
            element['bg'] = COLOR_DARK_MAIN if dark_mode else COLOR_MAIN