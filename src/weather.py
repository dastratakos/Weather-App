from PIL import Image, ImageTk
import tkinter as tk

from src.styles import *

class Weather(tk.Frame):
    def __init__(self, parent, dark_mode):
        tk.Frame.__init__(self, parent)

        self.dark_mode = dark_mode
        self.icon_name = None

        self.root = tk.Frame(parent)
        self.root.place(relx=0, rely=0.2, relwidth=0.5, relheight=0.275)

        self.icon = tk.Canvas(self.root, bd=0, highlightthickness=0)
        self.icon.place(relx=0, rely=0, width=ICON_SIZE, height=ICON_SIZE)

        self.l_temperature = tk.Label(self.root,
            font=(FONT, 50), anchor='nw', justify='left')
        self.l_temperature.place(x=65, rely=0)

        self.updateMode(dark_mode)

    def format(self, current):
        # open image
        self.icon_name = current['weather'][0]['icon']
        self.loadIcon()

        # update temperature
        self.l_temperature['text'] = f"{round(current['temp'])}°F"

    def loadIcon(self):
        if not self.icon_name: return

        raw_icon = (Image.open(ICON_DIR + self.icon_name + '.png')
                         .convert('RGBA')
                         .resize((ICON_SIZE, ICON_SIZE)))
        background = Image.new('RGB', raw_icon.size,
            COLOR_DARK_MAIN if self.dark_mode else COLOR_MAIN)
        background.paste(raw_icon, None, raw_icon)
        final_img = ImageTk.PhotoImage(background)

        self.icon.delete('all')
        self.icon.create_image(self.icon.winfo_width() / 2,
            self.icon.winfo_height() / 2, anchor='center', image=final_img)
        self.icon.image = final_img

    def updateMode(self, dark_mode):
        self.dark_mode = dark_mode

        self.root['bg'] = COLOR_DARK_MAIN if dark_mode else COLOR_MAIN
        self.l_temperature['fg'] = COLOR_DARK_TEXT_PRIMARY if dark_mode else COLOR_TEXT_PRIMARY
        self.l_temperature['bg'] = COLOR_DARK_MAIN if dark_mode else COLOR_MAIN

        self.loadIcon()