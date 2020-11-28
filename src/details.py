import tkinter as tk

from src.styles import *

class Details(tk.Frame):
    def __init__(self, parent, controller, dark_mode):
        tk.Frame.__init__(self, parent)

        self.root = tk.Frame(parent)
        self.root.place(relx=0.5, rely=0.2, relwidth=0.5, relheight=0.275)

        self.l_weather_details = tk.Label(self.root, font=(FONT, 15),
            anchor='nw', justify='left')
        self.l_weather_details.place(x=0, y=0, relheight=0.5)

        self.b_temperature = tk.Button(self.root, text='Temperature',
            font=(FONT, 15), command=lambda: controller.showStat('temp'))
        self.b_temperature.place(relx=0.05, rely=0.85, relwidth=0.35, height=30, anchor='sw')

        self.b_humidity = tk.Button(self.root, text='Humidity',
            font=(FONT, 15), command=lambda: controller.showStat('humidity'))
        self.b_humidity.place(relx=0.45, rely=0.85, relwidth=0.27, height=30, anchor='sw')

        self.b_wind = tk.Button(self.root, text='Wind',
            font=(FONT, 15), command=lambda: controller.showStat('wind'))
        self.b_wind.place(relx=0.77, rely=0.85, relwidth=0.18, height=30, anchor='sw')

        self.updateMode(dark_mode)
    
    def format(self, current):
        self.l_weather_details['text'] = \
            f"Feels like: {round(current['feels_like'])}°F\n" + \
            f"Humidity: {current['humidity']}%\n" + \
            f"Wind: {current['wind_speed']} mph"

    def updateMode(self, dark_mode):
        self.root['bg'] = COLOR_DARK_MAIN if dark_mode else COLOR_MAIN
        self.l_weather_details['fg'] = COLOR_DARK_TEXT_TERTIARY if dark_mode else COLOR_TEXT_TERTIARY
        self.l_weather_details['bg'] = COLOR_DARK_MAIN if dark_mode else COLOR_MAIN

        for button in [self.b_temperature, self.b_humidity, self.b_wind]:
            button['highlightbackground'] = COLOR_DARK_BUTTON if dark_mode else COLOR_DETAILS_BUTTON
            button['activebackground'] = COLOR_DARK_BUTTON if dark_mode else COLOR_DETAILS_BUTTON