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

HEIGHT = 700
WIDTH = 800

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
        return None
    return results[0]

def formatOneCallResponse(res):
    ### CURRENT WEATHER
    current = res['current']
    label_day['text'] = datetime.fromtimestamp(current['dt']).weekday()
    label_condition['text'] = current['weather'][0]['description'].capitalize()

    icon_name = current['weather'][0]['icon']
    open_image(icon_name)
    label_temperature['text'] = f"{round(current['temp'])}°F"

    label_weather_details['text'] = f"Feels like: {round(current['feels_like'])}°F\n" + \
                                    f"Humidity: {current['humidity']}%\n" + \
                                    f"Wind: {current['wind_speed']} mph"

    # HOURLY
    hourly = res['hourly'][:8]
    print('hourly', len(hourly))

    # DAILY
    daily = res['hourly'][:8]
    print(len(daily))

def buttonPressed(city_name, state_code, country_code):
    city_name, state_code, country_code = (city_name.strip(),
                                           state_code.strip(),
                                           country_code.strip())
    print(f'Input: {city_name}, {state_code}, {country_code}')

    # get 7-day forecast
    city = getCity(city_name, state_code, country_code)
    if not city: print('ERROR'); return
    lat, lon = city['coord']['lat'], city['coord']['lon']
    params = {'lat': lat, 'lon': lon, 'units': 'imperial', 'appid': APPID}
    res = requests.get(ONE_CALL_URL, params=params).json()

    with open('API_results/one_call.json', 'w') as f:
        json.dump(res, f, indent=4)

    label_location['text'] = city_name + \
                             (f', {state_code}' if state_code else '') + \
                             (f', {country_code}' if country_code else '')
    formatOneCallResponse(res)
    print()

def open_image(icon):
    img = ImageTk.PhotoImage(Image.open('./icons/' + icon + '.png').resize((60, 60)))
    weather_icon.delete('all')
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img

def temperaturePressed():
    pass

def feelsLikePressed():
    pass

def windPressed():
    pass

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
label_city.place(rely=0, relwidth=0.2, height=35)
entry_city = tk.Entry(input_frame, text='Saratoga', font=('Avenir Next', 20))
entry_city.place(rely=0, relx=0.25, relwidth=0.5, height=35)

label_state = tk.Label(input_frame, text='State:', font=('Avenir Next', 20),
    anchor='e', bg=COLOR_BLUE)
label_state.place(rely=0.3333, relwidth=0.2, height=35)
entry_state = tk.Entry(input_frame, text='CA', font=('Avenir Next', 20))
entry_state.place(rely=0.3333, relx=0.25, relwidth=0.5, height=35)

label_country = tk.Label(input_frame, text='Country:', font=('Avenir Next', 20),
    anchor='e', bg=COLOR_BLUE)
label_country.place(rely=0.6666, relwidth=0.2, height=35)
entry_country = tk.Entry(input_frame, text='USA', font=('Avenir Next', 20))
entry_country.place(rely=0.6666, relx=0.25, relwidth=0.5, height=35)

button_go = tk.Button(input_frame, text='GO', font=('Avenir Next', 20, 'bold'), fg=COLOR_GREEN,
    command=lambda: buttonPressed(entry_city.get(), entry_state.get(), entry_country.get()))
button_go.place(relx=0.8, rely=0.3, relwidth=0.2, relheight=0.4)

########## BOTTOM FRAME ##########
frame_output = tk.Frame(root, bg=COLOR_BLUE, bd=10)
frame_output.place(relx=0.5, rely=0.95, relwidth=0.85, relheight=0.65, anchor='s')

### OUTPUT FRAME 0
frame_output_0 = tk.Frame(frame_output, bg=COLOR_GREEN)
frame_output_0.place(relx=0, rely=0, relwidth=1, relheight=0.2)

label_location = tk.Label(frame_output_0, text='Saratoga, CA',
    font=('Avenir Next', 25), anchor='nw', justify='left', bg=COLOR_GREEN)
label_location.place(x=0, y=0, height=32)

label_day = tk.Label(frame_output_0, text='Tuesday',
    font=('Avenir Next', 15), anchor='nw', justify='left', bg='#ffffff')
label_day.place(x=0, y=32, height=20)

label_condition = tk.Label(frame_output_0, text='Partly cloudy',
    font=('Avenir Next', 15), anchor='nw', justify='left', bg='#888888')
label_condition.place(x=0, y=52, height=20)

### OUTPUT FRAME 1
frame_output_1 = tk.Frame(frame_output, bg=COLOR_GREEN)
frame_output_1.place(relx=0, rely=0.2, relwidth=1, relheight=0.55)

frame_weather = tk.Frame(frame_output_1, bg='red')
frame_weather.place(x=0, y=0, relheight=0.5, relwidth=0.5)

weather_icon = tk.Canvas(frame_weather, bg='white', bd=0, highlightthickness=0)
weather_icon.place(relx=0, rely=0, width=60, height=60)

label_temperature = tk.Label(frame_weather, text='70°F',
    font=('Avenir Next', 50), anchor='nw', justify='left', bg='brown')
label_temperature.place(x=60, rely=0)

##### WEATHER DETAILS FRAME

frame_weather_details = tk.Frame(frame_output_1, bg='yellow')
frame_weather_details.place(relx=0.5, y=0, relheight=0.5, relwidth=0.5)

label_weather_details = tk.Label(frame_weather_details,
    text='Feels like: 60°F\nHumidity: 77%\nWind: 4 mph',
    font=('Avenir Next', 15), anchor='nw', justify='left', bg='#888888')
label_weather_details.place(x=0, y=0, relheight=0.5)

button_temperature = tk.Button(frame_weather_details, text='Temperature',
    font=('Avenir Next', 15), command=lambda: temperaturePressed())
button_temperature.place(relx=0.05, rely=0.95, relwidth=0.3, height=30, anchor='sw')

button_feels_like = tk.Button(frame_weather_details, text='Feels like',
    font=('Avenir Next', 15), command=lambda: feelsLikePressed())
button_feels_like.place(relx=0.4, rely=0.95, relwidth=0.3, height=30, anchor='sw')

button_wind = tk.Button(frame_weather_details, text='Wind',
    font=('Avenir Next', 15), command=lambda: windPressed())
button_wind.place(relx=0.75, rely=0.95, relwidth=0.2, height=30, anchor='sw')

##### HOURLY FRAME

frame_hourly = tk.Frame(frame_output_1, bg='pink')
frame_hourly.place(x=0, rely=0.5, relheight=0.5, relwidth=1)

labels_hourly = []
for i in range(8):
    labels_hourly.append(tk.Label(frame_hourly, text=f'Hour {i}',
        font=('Avenir Next', 15), anchor='nw', justify='left', bg='#888888'))
    labels_hourly[-1].place(relx=(0.125 * i), y=0, relwidth=0.125, relheight=1)

### OUTPUT FRAME 2
frame_output_2 = tk.Frame(frame_output, bg='black')
frame_output_2.place(relx=0, rely=0.75, relwidth=1, relheight=0.25)

labels_daily = []
for i in range(8):
    labels_daily.append(tk.Label(frame_output_2, text=f'Day {i}',
        font=('Avenir Next', 15), anchor='nw', justify='left', bg='white'))
    labels_daily[-1].place(relx=(0.125 * i), y=0, relwidth=0.125, relheight=1)

root.mainloop()