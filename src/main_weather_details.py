import tkinter as tk

from src.styles import *

class MainWeatherDetails(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.root = tk.Frame(parent)
        self.root.place(relx=0.5, rely=0.2, relwidth=0.5, relheight=0.275)

        self.label_weather_details = tk.Label(self.root, fg=COLOR_GRAY,
            font=(FONT, 15), anchor='nw', justify='left')
        self.label_weather_details.place(x=0, y=0, relheight=0.5)

        self.button_temperature = tk.Button(self.root, text='Temperature',
            font=(FONT, 15), command=lambda: controller.showStat('temp'))
        self.button_temperature.place(relx=0.05, rely=0.85, relwidth=0.3, height=30, anchor='sw')

        self.button_humidity = tk.Button(self.root, text='Humidity',
            font=(FONT, 15), command=lambda: controller.showStat('humidity'))
        self.button_humidity.place(relx=0.4, rely=0.85, relwidth=0.3, height=30, anchor='sw')

        self.button_wind = tk.Button(self.root, text='Wind',
            font=(FONT, 15), command=lambda: controller.showStat('wind'))
        self.button_wind.place(relx=0.75, rely=0.85, relwidth=0.2, height=30, anchor='sw')
    
    def format(self, current):
        self.label_weather_details['text'] = \
            f"Feels like: {round(current['feels_like'])}°F\n" + \
            f"Humidity: {current['humidity']}%\n" + \
            f"Wind: {current['wind_speed']} mph"