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
import pprint as pp

from PIL import Image, ImageTk
import requests
import tkinter as tk
from tkinter import font

pprint = pp.PrettyPrinter(indent=4)

HEIGHT = 500
WIDTH = 600

COLOR_BLUE = '#80c1ff'

WEATHER_KEY = 'eaee5bbe92bd1ce768a5927848974db2'
URL = 'https://api.openweathermap.org/data/2.5/weather'
# URL = 'https://api.openweathermap.org/data/2.5/forecast'

def format_response(res):
    try:
        city = res['name']+ ', ' + res['sys']['country']
        desc = res['weather'][0]['description']
        temp = res['main']['temp']

        return f'City: {city}\nConditions: {desc}\nTemperature (°F) {temp}'
    except:
        return 'There was a problem retrieving the information'

def get_weather(city):
    print('City:', city)
    params = {'appid': WEATHER_KEY, 'q': city, 'units': 'imperial'}
    response = requests.get(URL, params=params)
    res = response.json()
    pp.pprint(res)

    label['text'] = format_response(res)

    icon_name = res['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon):
    size = int(frame2.winfo_height() * 0.25)
    img = ImageTk.PhotoImage(Image.open('./icons/' + icon + '.png').resize((size, size)))
    weather_icon.delete('all')
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img

root = tk.Tk()

canvas =tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='./background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame1 = tk.Frame(root, bg=COLOR_BLUE)
frame1.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame1, font=('Avenir Next', 20))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame1, text='Get weather', font=('Avenir Next', 20),
    command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

frame2 = tk.Frame(root, bg=COLOR_BLUE, bd=10)
frame2.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(frame2, font=('Avenir Next', 20), anchor='nw', justify='left')
label.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(label, bg='white', bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

root.mainloop()