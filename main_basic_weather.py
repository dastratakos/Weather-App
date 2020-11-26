from PIL import Image, ImageTk
import tkinter as tk

ICON_SIZE = 60

class MainBasicWeather(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.root = tk.Frame(parent)
        self.root.place(relx=0, rely=0.2, relwidth=0.25, relheight=0.275)

        self.weather_icon = tk.Canvas(self.root, bd=0, highlightthickness=0)
        self.weather_icon.place(relx=0, rely=0, width=ICON_SIZE, height=ICON_SIZE)

        self.label_temperature = tk.Label(self.root,
            font=('Avenir Next', 50), anchor='nw', justify='left')
        self.label_temperature.place(x=65, rely=0)

    def format(self, current):
        # open image
        icon_name = current['weather'][0]['icon']
        img = ImageTk.PhotoImage(Image.open(f'./resources/{icon_name}.png')
                                      .resize((ICON_SIZE, ICON_SIZE)))
        self.weather_icon.delete('all')
        self.weather_icon.create_image(self.weather_icon.winfo_width() / 2, self.weather_icon.winfo_height() / 2,
            anchor='center', image=img)
        self.weather_icon.image = img

        # update temperature
        self.label_temperature['text'] = f"{round(current['temp'])}°F"