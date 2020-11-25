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
from datetime import datetime
import json
import pprint as pp

# from geocodio import GeocodioClient
from PIL import Image, ImageTk
import requests
import tkinter as tk

pprint = pp.PrettyPrinter(indent=4)

HEIGHT = 800
WIDTH = 600

COLOR_BLUE = '#80c1ff'
COLOR_GREEN = '#3bb143'

# GEOCODE = '5575ab1bab159c5d9fcfcd99c517fdd99777ab7'

APPID = 'eaee5bbe92bd1ce768a5927848974db2'
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'
FORECAST_URL = 'https://api.openweathermap.org/data/2.5/forecast/daily'
ONE_CALL_URL = 'https://api.openweathermap.org/data/2.5/onecall'

with open('city.list.json') as f:
    city_list = json.load(f)

def formatCurrentWeather(current):
    try:
        city = res['name']+ ', ' + res['sys']['country']
        desc = res['weather'][0]['description']
        temp = res['main']['temp']

        return f'City: {city}\nConditions: {desc}\nTemperature (°F) {temp}'
    except:
        return 'There was a problem retrieving the information'

def get_day(res):
    for day in res['daily']:
        dt = datetime.fromtimestamp(day['dt'])
        print(dt.strftime('%A'))

def getLatLon(city_name, state_code, country_code):
    results = [x for x in city_list
                if (not city_name or x['name'] == city_name) and
                   (not state_code or x['state'] == state_code) and
                   (not country_code or x['country'] == country_code)]
    if len(results) == 0:
        print(f'\tNo results')
        return None, None
    elif len(results) > 1:
        print(f'\t{len(results)} results')
        for result in results[:10]:
            print(f"\t\t{result['name']}, {result['state']}, {result['country']}")
        if len(results) > 10:
            print('\t\t...')
        return None, None
    else:
        lat, lon = results[0]['coord']['lat'], results[0]['coord']['lon']
        print(f"\tlatitude:   {lat}")
        print(f"\tlongitutde: {lon}")
        return lat, lon

def buttonPressed(city_name, state_code, country_code):
    city_name, state_code, country_code = (city_name.strip(),
                                           state_code.strip(),
                                           country_code.strip())
    print(f'Input: {city_name}, {state_code}, {country_code}')

    # get 7-day forecast
    lat, lon = getLatLon(city_name, state_code, country_code)
    if not (lat and lon):
        print('ERROR')
        return
    params = {'lat': lat, 'lon': lon, 'units': 'imperial', 'appid': APPID}
    res = requests.get(ONE_CALL_URL, params=params).json()

    get_day(res)
    # with open('one_call.json', 'w+') as f:
    #     json.dump(res, f, indent=4)
    # pp.pprint(res)
    # label['text'] = format_response(res)

    # icon_name = res['weather'][0]['icon']
    # open_image(icon_name)
    print()

def open_image(icon):
    size = int(output_frame.winfo_height() * 0.25)
    img = ImageTk.PhotoImage(Image.open('./icons/' + icon + '.png').resize((size, size)))
    weather_icon.delete('all')
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='./background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

########## TOP FRAME ##########
input_frame = tk.Frame(root, bg=COLOR_BLUE, bd=10)
input_frame.place(relx=0.5, rely=0.05, relwidth=0.85, relheight=0.2, anchor='n')

label_city = tk.Label(input_frame, text='City:', font=('Avenir Next', 20),
    anchor='e', bg=COLOR_BLUE)
# label_city.place(rely=0, relwidth=0.2, height=35)
label_city.grid(row=1, column=1)
entry_city = tk.Entry(input_frame, text='Saratoga', font=('Avenir Next', 20))
# entry_city.place(rely=0, relx=0.25, relwidth=0.5, height=35)
entry_city.grid(row=1, column=2)

label_state = tk.Label(input_frame, text='State:', font=('Avenir Next', 20),
    anchor='e', bg=COLOR_BLUE)
# label_state.place(rely=0.32, relwidth=0.2, height=35)
label_state.grid(row=2, column=1)
entry_state = tk.Entry(input_frame, text='CA', font=('Avenir Next', 20))
# entry_state.place(rely=0.32, relx=0.25, relwidth=0.5, height=35)
entry_state.grid(row=2, column=2)

label_country = tk.Label(input_frame, text='Country:', font=('Avenir Next', 20),
    anchor='e', bg=COLOR_BLUE)
# label_country.place(rely=0.7, relwidth=0.2, height=35)
label_country.grid(row=3, column=1)
entry_country = tk.Entry(input_frame, text='USA', font=('Avenir Next', 20))
# entry_country.place(rely=0.7, relx=0.25, relwidth=0.5, height=35)
entry_country.grid(row=3, column=2)

button = tk.Button(input_frame, text='GO', font=('Avenir Next', 20, 'bold'), fg=COLOR_GREEN,
    command=lambda: buttonPressed(entry_city.get(), entry_state.get(), entry_country.get()))
# button.place(relx=0.8, rely=0.3, relwidth=0.2, relheight=0.4)
button.grid(row=1, column=3, rowspan=3)

########## BOTTOM FRAME ##########
# output_frame = tk.Frame(root, bg=COLOR_BLUE, bd=10)
# output_frame.place(relx=0.5, rely=0.25, relwidth=0.85, relheight=0.6, anchor='n')

# label = tk.Label(output_frame, font=('Avenir Next', 20), anchor='nw', justify='left')
# label.place(relwidth=1, relheight=1)

# weather_icon = tk.Canvas(label, bg='white', bd=0, highlightthickness=0)
# weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

root.mainloop()