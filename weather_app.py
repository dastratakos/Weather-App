"""
file: WeatherApp.py
author: Dean Stratakos
date: November 23, 2020
-----------------------
A weather app built using Python that provides a GUI.

References:
    https://www.youtube.com/watch?v=D8-snVfekto&t=204s
    https://github.com/KeithGalli/GUI
"""
###### IMPORT BUILT-IN LIBRARIES
from datetime import datetime, time
import json
import requests

###### IMPORT THIRD-PARTY LIBRARIES
import tkinter as tk

###### IMPORT CUSTOM COMPONENTS
from src.styles         import *
from src.curtain        import Curtain
from src.daily          import Daily
from src.details        import Details
from src.footer         import Footer
from src.headline       import Headline
from src.hourly         import Hourly
from src.search_module  import SearchModule
from src.theme          import Theme
from src.weather        import Weather

HEIGHT = 700
WIDTH = 800
MIN_HEIGHT = 650
MIN_WIDTH = 650

APPID = 'eaee5bbe92bd1ce768a5927848974db2'
ONE_CALL_URL = 'https://api.openweathermap.org/data/2.5/onecall'
class Main(tk.Frame):
    def __init__(self, parent, dark_mode):
        tk.Frame.__init__(self, parent)

        self.root = tk.Frame(parent, bd=10)
        self.root.place(relx=0.5, rely=0.95, relwidth=0.85, relheight=0.65, anchor='s')

        self.header = Headline(self.root, dark_mode)
        self.basic_weather = Weather(self.root, dark_mode)
        self.weather_details = Details(self.root, self, dark_mode)
        self.hourly = Hourly(self.root, dark_mode)
        self.daily = Daily(self.root, dark_mode)

        self.curtain = Curtain(self.root, dark_mode)
        self.curtain_exists = True

        self.updateMode(dark_mode)

    def formatOneCallResponse(self, city, res):
        if self.curtain_exists:
            self.curtain.l_home.destroy()
            self.curtain_exists = False

        self.header.format(city, res['current'])
        self.basic_weather.format(res['current'])
        self.weather_details.format(res['current'])

        self.hourly.format(res['hourly'])

        self.daily.format(res['daily'])

    def showStat(self, mode):
        self.hourly.showStat(mode)

    def updateMode(self, dark_mode):
        self.root['bg'] = COLOR_DARK_MAIN if dark_mode else COLOR_MAIN

        if self.curtain_exists:
            self.curtain.updateMode(dark_mode)
        
        self.header.updateMode(dark_mode)
        self.basic_weather.updateMode(dark_mode)
        self.weather_details.updateMode(dark_mode)
        self.hourly.updateMode(dark_mode)
        self.daily.updateMode(dark_mode)

class WeatherApp(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)

        self.root = root
        self.root.geometry(f'{WIDTH}x{HEIGHT}')
        self.root.minsize(MIN_WIDTH, MIN_HEIGHT)

        # use Dark Mode if the app is started before 6AM or after 6PM
        self.dark_mode = (datetime.now().time() < time(6, 0, 0) or
                          datetime.now().time() > time(18, 0, 0))
        self.root.configure(bg=(COLOR_DARK_BACKGROUND if self.dark_mode else COLOR_BACKGROUND))
        
        self.search_module = SearchModule(self.root, self, self.dark_mode)
        self.main = Main(self.root, self.dark_mode)
        self.footer = Footer(self.root, self.dark_mode)
        self.theme = Theme(self.root, self, self.dark_mode)

    def buttonSearchPressed(self, city_name, state_code, country_code, internet=True):
        city_name, state_code, country_code = (city_name.strip().title(),
                                            state_code.strip().upper(),
                                            country_code.strip().upper())
        print(f'Input: {city_name}, {state_code}, {country_code}')

        # get 7-day forecast
        city = self.search_module.getCity(city_name, state_code, country_code)
        if not city: print('No unique city'); return
        print(f"Output: {city['name']}, {city['state']}, {city['country']}")
        if internet:
            lat, lon = city['coord']['lat'], city['coord']['lon']
            params = {'lat': lat, 'lon': lon, 'units': 'imperial', 'appid': APPID}
            res = requests.get(ONE_CALL_URL, params=params).json()
        else:
            with open('./open-weather-app/one_call.json') as f:
                res = json.load(f)

        self.main.formatOneCallResponse(city, res)
        print()

    def buttonThemePressed(self):
        self.dark_mode = not self.dark_mode
        
        self.root.configure(bg=(COLOR_DARK_BACKGROUND if self.dark_mode else COLOR_BACKGROUND))
        self.theme.updateMode(self.dark_mode)
        self.search_module.updateMode(self.dark_mode)
        self.main.updateMode(self.dark_mode)
        self.footer.updateMode(self.dark_mode)

def main():
    root = tk.Tk(className='weather app')

    WeatherApp(root)

    root.mainloop()

if __name__ == '__main__':
    main()