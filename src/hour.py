from datetime import datetime

import tkinter as tk

from src.styles import *

class Hour(tk.Frame):
    def __init__(self, parent, index, dark_mode):
        tk.Frame.__init__(self, parent)

        self.dark_mode = dark_mode

        self.hour = ''
        self.stats = {
            'temp': {'text': '', 'size': 30},
            'humidity': {'text': '', 'size': 25},
            'wind': {'text': '', 'size': 20}
        }

        self.root = tk.Frame(parent)
        self.root.place(relx=(0.125 * index), y=0, relwidth=0.125, relheight=1)

        self.l_stat = tk.Label(self.root, font=(FONT, 30))
        self.l_stat.place(relx=0, rely=0.5, relwidth=1, height=80, anchor='w')

        self.l_time = tk.Label(self.root, font=(FONT, 15), anchor='n')
        self.l_time.place(relx=0, rely=0, relwidth=1, height=20)

        self.updateMode(dark_mode)

    def format(self, res):
        """
        Args:
            res (dict): sub-response that contains information for a single hour
        """
        # update hour
        self.hour = datetime.fromtimestamp(res['dt']).strftime('%-I %p')

        # update stats
        self.stats['temp']['text'] = f"{round(res['temp'])}°"
        self.stats['humidity']['text'] = f"{res['humidity']}%"
        self.stats['wind']['text'] = f"{res['wind_speed']}\nmph"

    def showStat(self, stat):
        self.l_time['text'] = self.hour
        self.l_stat['text'] = self.stats[stat]['text']
        self.l_stat['font'] = (FONT, self.stats[stat]['size'])

    def updateMode(self, dark_mode):
        self.dark_mode = dark_mode

        self.root['bg'] = COLOR_DARK_MAIN if dark_mode else COLOR_MAIN

        self.l_time['fg'] = COLOR_DARK_TEXT_QUATERNARY if dark_mode else COLOR_TEXT_QUATERNARY
        self.l_time['bg'] = COLOR_DARK_MAIN if dark_mode else COLOR_MAIN

        self.l_stat['fg'] = COLOR_DARK_TEXT_PRIMARY if dark_mode else COLOR_TEXT_PRIMARY
        self.l_stat['bg'] = COLOR_DARK_MAIN if dark_mode else COLOR_MAIN
        