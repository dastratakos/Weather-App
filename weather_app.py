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
# import pprint as pp
# pprint = pp.PrettyPrinter(indent=4)

###### IMPORT THIRD-PARTY LIBRARIES
import requests
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
MIN_HEIGHT = 600
MIN_WIDTH = 600

APPID = 'eaee5bbe92bd1ce768a5927848974db2'
ONE_CALL_URL = 'https://api.openweathermap.org/data/2.5/onecall'
class Main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.root = tk.Frame(parent, bd=10)
        self.root.place(relx=0.5, rely=0.95, relwidth=0.85, relheight=0.65, anchor='s')

        self.header = Headline(self.root)
        self.basic_weather = Weather(self.root)
        self.weather_details = Details(self.root, self)
        self.hourly = Hourly(self.root)
        self.daily = Daily(self.root)
        self.curtain = Curtain(self.root)

    def formatOneCallResponse(self, res):
        self.curtain.root.destroy()

        self.header.format(res['current'])
        self.basic_weather.format(res['current'])
        self.weather_details.format(res['current'])

        self.hourly.format(res['hourly'])

        self.daily.format(res['daily'])

    def showStat(self, mode):
        self.hourly.showStat(mode)

    def updateMode(self, darkTheme):
        self.root['bg'] = COLOR_DARK_GRAY if darkTheme else COLOR_BLUE
        self.curtain.updateMode(darkTheme)

class WeatherApp(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)

        self.root = root

        self.dark_mode = False
        
        self.search_module = SearchModule(self.root, self)
        self.main = Main(self.root)
        self.footer = Footer(self.root)
        self.theme = Theme(self.root, self)

    def buttonSearchPressed(self, city_name, state_code, country_code):
        city_name, state_code, country_code = (city_name.strip().title(),
                                            state_code.strip().upper(),
                                            country_code.strip().upper())
        print(f'Input: {city_name}, {state_code}, {country_code}')

        # get 7-day forecast
        city = self.search_module.getCity(city_name, state_code, country_code)
        if not city: print('No unique city'); return
        print(f"Output: {city['name']}, {city['state']}, {city['country']}")
        lat, lon = city['coord']['lat'], city['coord']['lon']
        params = {'lat': lat, 'lon': lon, 'units': 'imperial', 'appid': APPID}
        res = requests.get(ONE_CALL_URL, params=params).json()

        self.main.header.label_location['text'] = city['name'] + \
            (f", {city['state']}" if city['state'] else '') + \
            (f", {city['country']}" if city['country'] else '')

        self.main.formatOneCallResponse(res)
        print()

    def buttonThemePressed(self):
        self.dark_mode = not self.dark_mode

        self.root.configure(bg=(COLOR_DARK_GRAY if self.dark_mode else COLOR_BLUE))
        self.theme.updateMode(self.dark_mode)
        self.search_module.updateMode(self.dark_mode)
        self.main.updateMode(self.dark_mode)
        self.footer.updateMode(self.dark_mode)

def main(): 
    root = tk.Tk(className='weather app')
    root.geometry(f'{WIDTH}x{HEIGHT}')
    root.configure(bg=COLOR_BLUE)
    root.minsize(MIN_WIDTH, MIN_HEIGHT)

    WeatherApp(root)

    root.mainloop()

if __name__ == '__main__':
    main()