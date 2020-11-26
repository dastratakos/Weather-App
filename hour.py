from datetime import datetime

import tkinter as tk

from styles import *

class Hour(tk.Frame):
    def __init__(self, parent, index):
        tk.Frame.__init__(self, parent)

        self.hour = ''
        self.stats = {
            'temp': {'text': '', 'size': 30},
            'humidity': {'text': '', 'size': 25},
            'wind': {'text': '', 'size': 20}
        }

        self.root = tk.Frame(parent)
        self.root.place(relx=(0.125 * index), y=0, relwidth=0.125, relheight=1)

        self.label_time = tk.Label(self.root,
            fg=COLOR_LIGHT_GRAY, font=(FONT, 15), anchor='n')
        self.label_time.place(relx=0, rely=0, relwidth=1, height=20)

        self.label_stat = tk.Label(self.root,
            font=(FONT, 30))
        self.label_stat.place(relx=0, rely=0.5, relwidth=1, height=80, anchor='w')

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
        self.label_time['text'] = self.hour
        self.label_stat['text'] = self.stats[stat]['text']
        self.label_stat['font'] = (FONT, self.stats[stat]['size'])