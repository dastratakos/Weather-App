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

from PIL import Image, ImageTk
import requests
import tkinter as tk

pprint = pp.PrettyPrinter(indent=4)

HEIGHT = 700
WIDTH = 800

COLOR_WHITE = '#efefef'
COLOR_GRAY = '#767676'
COLOR_LIGHT_GRAY = '#989898'
COLOR_DARK_GRAY = '#444444'
COLOR_BLUE = '#4b80ac' #'#80c1ff'
COLOR_GREEN = '#3bb143'

APPID = 'eaee5bbe92bd1ce768a5927848974db2'
ONE_CALL_URL = 'https://api.openweathermap.org/data/2.5/onecall'

with open('city.list.json') as f:
    city_list = json.load(f)

hourly_memory = []

def getCity(city_name, state_code, country_code):
    results = [x for x in city_list
                if (not city_name or x['name'] == city_name) and
                   (not state_code or x['state'] == state_code) and
                   (not country_code or x['country'] == country_code)]
    if len(results) == 0:
        print(f'\tNo results')
        return None
    elif len(results) > 1:
        print(f'\t{len(results)} results')
        for result in results[:10]:
            print(f"\t\t{result['name']}, {result['state']}, {result['country']}")
        if len(results) > 10:
            print('\t\t...')
        for result in results:
            if (result['name'] != results[0]['name']) or \
               (result['state'] != results[0]['state']) or \
               (result['country'] != results[0]['country']):
                return None
    return results[0]

def formatHourly(stat):
    for i, hour_entry in enumerate(hourly_memory):
        containers_hourly[i]['stat']['text'] = hour_entry[stat]
        if stat == 'temp':
            containers_hourly[i]['stat']['font'] = ('Avenir Next', 30)
        if stat == 'humidity':
            containers_hourly[i]['stat']['font'] = ('Avenir Next', 25)
        if stat == 'wind':
            containers_hourly[i]['stat']['font'] = ('Avenir Next', 20)

def formatOneCallResponse(res):
    ### CURRENT WEATHER
    current = res['current']
    label_day['text'] = datetime.fromtimestamp(current['dt']).strftime('%A')
    label_condition['text'] = current['weather'][0]['description'].capitalize()

    icon_name = current['weather'][0]['icon']
    open_image(weather_icon, icon_name)
    label_temperature['text'] = f"{round(current['temp'])}°F"

    label_weather_details['text'] = f"Feels like: {round(current['feels_like'])}°F\n" + \
                                    f"Humidity: {current['humidity']}%\n" + \
                                    f"Wind: {current['wind_speed']} mph"

    # HOURLY
    hourly = res['hourly']
    hourly_memory.clear()
    for i in range(8):
        hourly_memory.append({
            'hour': datetime.fromtimestamp(hourly[i]['dt']).strftime('%-I %p'),
            'temp': f"{round(hourly[i]['temp'])}°",
            'humidity': f"{hourly[i]['humidity']}%",
            'wind': f"{hourly[i]['wind_speed']}\nmph"
        })
        containers_hourly[i]['label']['text'] = hourly_memory[-1]['hour']

    formatHourly('temp')

    # DAILY
    daily = res['daily']
    for i in range(8):
        day = datetime.fromtimestamp(daily[i]['dt']).strftime('%a %-d')
        containers_daily[i]['label']['text'] = day

        icon_name = daily[i]['weather'][0]['icon']
        open_image(containers_daily[i]['icon'], icon_name)

        containers_daily[i]['temp']['text'] = f"{round(daily[i]['temp']['max'])}° / " + \
                                              f"{round(daily[i]['temp']['min'])}°"


def buttonPressed(city_name, state_code, country_code):
    city_name, state_code, country_code = (city_name.strip().title(),
                                           state_code.strip().upper(),
                                           country_code.strip().upper())
    print(f'Input: {city_name}, {state_code}, {country_code}')

    # get 7-day forecast
    city = getCity(city_name, state_code, country_code)
    if not city: print('No unique city'); return
    print(f"Output: {city['name']}, {city['state']}, {city['country']}")
    lat, lon = city['coord']['lat'], city['coord']['lon']
    params = {'lat': lat, 'lon': lon, 'units': 'imperial', 'appid': APPID}
    res = requests.get(ONE_CALL_URL, params=params).json()

    # with open('API_results/one_call.json', 'w') as f:
    #     json.dump(res, f, indent=4)

    label_location['text'] = city['name'] + \
                             (f", {city['state']}" if city['state'] else '') + \
                             (f", {city['country']}" if city['country'] else '')

    frame_hide.destroy()

    formatOneCallResponse(res)
    print()

def open_image(canvas, icon):
    img = ImageTk.PhotoImage(Image.open('./icons/' + icon + '.png').resize((60, 60)))
    canvas.delete('all')
    canvas.create_image(canvas.winfo_width() / 2, canvas.winfo_height() / 2, anchor='center', image=img)
    canvas.image = img

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
    anchor='e', bg=COLOR_BLUE, fg=COLOR_WHITE)
label_city.place(rely=0, relwidth=0.2, height=35)
entry_city = tk.Entry(input_frame, text='Saratoga', font=('Avenir Next', 20),
    fg=COLOR_DARK_GRAY)
entry_city.place(rely=0, relx=0.25, relwidth=0.5, height=35)

label_state = tk.Label(input_frame, text='State:', font=('Avenir Next', 20),
    anchor='e', bg=COLOR_BLUE, fg=COLOR_WHITE)
label_state.place(rely=0.3333, relwidth=0.2, height=35)
entry_state = tk.Entry(input_frame, text='CA', font=('Avenir Next', 20),
    fg=COLOR_DARK_GRAY)
entry_state.place(rely=0.3333, relx=0.25, relwidth=0.5, height=35)

label_country = tk.Label(input_frame, text='Country:', font=('Avenir Next', 20),
    anchor='e', bg=COLOR_BLUE, fg=COLOR_WHITE)
label_country.place(rely=0.6666, relwidth=0.2, height=35)
entry_country = tk.Entry(input_frame, text='USA', font=('Avenir Next', 20),
    fg=COLOR_DARK_GRAY)
entry_country.place(rely=0.6666, relx=0.25, relwidth=0.5, height=35)

button_go = tk.Button(input_frame, text='GO', font=('Avenir Next', 20, 'bold'), fg=COLOR_GREEN,
    command=lambda: buttonPressed(entry_city.get(), entry_state.get(), entry_country.get()))
button_go.place(relx=0.8, rely=0.3, relwidth=0.2, relheight=0.4)

########## BOTTOM FRAME ##########
frame_output = tk.Frame(root, bd=10)
frame_output.place(relx=0.5, rely=0.95, relwidth=0.85, relheight=0.65, anchor='s')

### OUTPUT FRAME 0
frame_output_0 = tk.Frame(frame_output)
frame_output_0.place(relx=0, rely=0, relwidth=1, relheight=0.2)

label_location = tk.Label(frame_output_0, fg=COLOR_GRAY,
    font=('Avenir Next', 25), anchor='nw', justify='left')
label_location.place(x=0, y=0, height=32)

label_day = tk.Label(frame_output_0, fg=COLOR_GRAY,
    font=('Avenir Next', 15), anchor='nw', justify='left')
label_day.place(x=0, y=32, height=20)

label_condition = tk.Label(frame_output_0, fg=COLOR_GRAY,
    font=('Avenir Next', 15), anchor='nw', justify='left')
label_condition.place(x=0, y=52, height=20)

### OUTPUT FRAME 1
frame_output_1 = tk.Frame(frame_output)
frame_output_1.place(relx=0, rely=0.2, relwidth=1, relheight=0.55)

frame_weather = tk.Frame(frame_output_1)
frame_weather.place(x=0, y=0, relheight=0.5, relwidth=0.5)

weather_icon = tk.Canvas(frame_weather, bd=0, highlightthickness=0)
weather_icon.place(relx=0, rely=0, width=60, height=60)

label_temperature = tk.Label(frame_weather,
    font=('Avenir Next', 50), anchor='nw', justify='left')
label_temperature.place(x=65, rely=0)

##### WEATHER DETAILS FRAME

frame_weather_details = tk.Frame(frame_output_1)
frame_weather_details.place(relx=0.5, y=0, relheight=0.5, relwidth=0.5)

label_weather_details = tk.Label(frame_weather_details, fg=COLOR_GRAY,
    font=('Avenir Next', 15), anchor='nw', justify='left')
label_weather_details.place(x=0, y=0, relheight=0.5)

button_temperature = tk.Button(frame_weather_details, text='Temperature',
    font=('Avenir Next', 15), command=lambda: formatHourly('temp'))
button_temperature.place(relx=0.05, rely=0.85, relwidth=0.3, height=30, anchor='sw')

button_humidity = tk.Button(frame_weather_details, text='Humidity',
    font=('Avenir Next', 15), command=lambda: formatHourly('humidity'))
button_humidity.place(relx=0.4, rely=0.85, relwidth=0.3, height=30, anchor='sw')

button_wind = tk.Button(frame_weather_details, text='Wind',
    font=('Avenir Next', 15), command=lambda: formatHourly('wind'))
button_wind.place(relx=0.75, rely=0.85, relwidth=0.2, height=30, anchor='sw')

##### HOURLY FRAME

frame_hourly = tk.Frame(frame_output_1, bg=COLOR_GRAY)
frame_hourly.place(x=0, rely=0.5, relheight=0.5, relwidth=1)

containers_hourly = []
for i in range(8):
    containers_hourly.append({
        'frame': tk.Frame(frame_hourly)
    })
    containers_hourly[-1]['frame'].place(relx=(0.125 * i), y=0, relwidth=0.125, relheight=1)

    containers_hourly[-1]['label'] = tk.Label(containers_hourly[-1]['frame'],
        fg=COLOR_LIGHT_GRAY, font=('Avenir Next', 15), anchor='n')
    containers_hourly[-1]['label'].place(relx=0, rely=0, relwidth=1, height=20)

    containers_hourly[-1]['stat'] = tk.Label(containers_hourly[-1]['frame'],
        font=('Avenir Next', 30))
    containers_hourly[-1]['stat'].place(relx=0, rely=0.5, relwidth=1, height=80, anchor='w')

### OUTPUT FRAME 2
frame_output_2 = tk.Frame(frame_output)
frame_output_2.place(relx=0, rely=0.75, relwidth=1, relheight=0.25)

containers_daily = []
for i in range(8):
    containers_daily.append({
        'frame': tk.Frame(frame_output_2)
    })
    containers_daily[-1]['frame'].place(relx=(0.125 * i), y=0, relwidth=0.125, relheight=1)

    containers_daily[-1]['label'] = tk.Label(containers_daily[-1]['frame'],
        fg=COLOR_LIGHT_GRAY, font=('Avenir Next', 15), anchor='n')
    containers_daily[-1]['label'].place(relx=0, rely=0, relwidth=1, height=20)

    containers_daily[-1]['icon'] = tk.Canvas(containers_daily[-1]['frame'],
        bd=0, highlightthickness=0)
    containers_daily[-1]['icon'].place(relx=0, rely=0.5, relwidth=1, height=60, anchor='w')

    containers_daily[-1]['temp'] = tk.Label(containers_daily[-1]['frame'],
        font=('Avenir Next', 15), anchor='n')
    containers_daily[-1]['temp'].place(relx=0.5, rely=1, relwidth=1, height=20, anchor='s')

frame_hide = tk.Frame(root, bd=10)
frame_hide.place(relx=0.5, rely=0.95, relwidth=0.85, relheight=0.65, anchor='s')

label_home = tk.Label(frame_hide, text="Enter a city...", fg=COLOR_LIGHT_GRAY,
    font=('Avenir Next', 20), anchor='center')
label_home.place(relwidth=1, relheight=1)

label_footer = tk.Label(root, text="Powered by OpenWeatherMap", bg=COLOR_BLUE,
    font=('Avenir Next', 12), anchor='s')
label_footer.place(relx=0.5, rely=1, relwidth=1, height=20, anchor='s')

root.mainloop()