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
from datetime import datetime
# import pprint as pp
# pprint = pp.PrettyPrinter(indent=4)

###### IMPORT THIRD-PARTY LIBRARIES
from PIL import Image, ImageTk
import requests
import tkinter as tk

###### IMPORT CUSTOM COMPONENTS
from colors import *
import curtain
import footer
import main_basic_weather
import main_daily
import main_header
import main_hourly
import main_weather_details
import search_module

HEIGHT = 700
WIDTH = 800

APPID = 'eaee5bbe92bd1ce768a5927848974db2'
ONE_CALL_URL = 'https://api.openweathermap.org/data/2.5/onecall'
class Main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.root = tk.Frame(parent, bd=10)
        self.root.place(relx=0.5, rely=0.95, relwidth=0.85, relheight=0.65, anchor='s')

        self.header = main_header.MainHeader(self.root)
        self.basic_weather = main_basic_weather.MainBasicWeather(self.root)
        self.weather_details = main_weather_details.MainWeatherDetails(self.root, self)
        self.hourly = main_hourly.MainHourly(self.root)
        self.daily = main_daily.MainDaily(self.root)

    def open_image(self, canvas, icon):
        img = ImageTk.PhotoImage(Image.open('./resources/' + icon + '.png').resize((60, 60)))
        canvas.delete('all')
        canvas.create_image(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
            anchor='center', image=img)
        canvas.image = img

    def formatOneCallResponse(self, res):
        current = res['current']
        self.header.formatHeader(current)
        self.basic_weather.format(current)

        self.weather_details.label_weather_details['text'] = \
            f"Feels like: {round(current['feels_like'])}°F\n" + \
            f"Humidity: {current['humidity']}%\n" + \
            f"Wind: {current['wind_speed']} mph"

        # HOURLY
        hourly = res['hourly']
        self.hourly.hourly_memory.clear()
        for i in range(8):
            self.hourly.hourly_memory.append({
                'hour': datetime.fromtimestamp(hourly[i]['dt']).strftime('%-I %p'),
                'temp': f"{round(hourly[i]['temp'])}°",
                'humidity': f"{hourly[i]['humidity']}%",
                'wind': f"{hourly[i]['wind_speed']}\nmph"
            })
            self.hourly.containers_hourly[i]['label']['text'] = self.hourly.hourly_memory[-1]['hour']

        self.hourly.formatHourly('temp')

        # DAILY
        daily = res['daily']
        for i in range(8):
            day = datetime.fromtimestamp(daily[i]['dt']).strftime('%a %-d')
            self.daily.containers_daily[i]['label']['text'] = day

            icon_name = daily[i]['weather'][0]['icon']
            self.open_image(self.daily.containers_daily[i]['icon'], icon_name)

            self.daily.containers_daily[i]['temp']['text'] = f"{round(daily[i]['temp']['max'])}° / " + \
                                                f"{round(daily[i]['temp']['min'])}°"

    def formatHourly(self, mode):
        self.hourly.formatHourly(mode)

class WeatherApp(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        
        self.search_module = search_module.SearchModule(root, self)
        self.main = Main(root)
        self.curtain = curtain.Curtain(root)
        self.footer = footer.Footer(root)

    def buttonPressed(self, city_name, state_code, country_code):
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

        self.curtain.root.destroy()

        self.main.formatOneCallResponse(res)
        print()

def main(): 
    root = tk.Tk()

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    background_image = tk.PhotoImage(file='./resources/background.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    WeatherApp(root)

    root.mainloop()

if __name__ == '__main__':
    main()