from datetime import datetime

from PIL import Image, ImageTk
import tkinter as tk

from src.styles import *

class Day(tk.Frame):
    def __init__(self, parent, index):
        tk.Frame.__init__(self, parent)

        self.root = tk.Frame(parent)
        self.root.place(relx=(0.125 * index), y=0, relwidth=0.125, relheight=1)

        self.label_date = tk.Label(self.root, fg=COLOR_LIGHT_GRAY,
            font=(FONT, 15), anchor='n')
        self.label_date.place(relx=0, rely=0, relwidth=1, height=20)

        self.icon = tk.Canvas(self.root, bd=0, highlightthickness=0)
        self.icon.place(relx=0, rely=0.5, relwidth=1, height=ICON_SIZE, anchor='w')

        self.label_temps = tk.Label(self.root, font=(FONT, 15), anchor='n')
        self.label_temps.place(relx=0.5, rely=1, relwidth=1, height=20, anchor='s')

    def format(self, res):
        """
        Args:
            res (dict): sub-response that contains information for a single day
        """
        # update date
        self.label_date['text'] = datetime.fromtimestamp(res['dt']).strftime('%a %-d')

        # open image
        icon_name = res['weather'][0]['icon']
        img = ImageTk.PhotoImage(Image.open(ICON_DIR + icon_name + '.png')
                                      .resize((ICON_SIZE, ICON_SIZE)))
        self.icon.delete('all')
        self.icon.create_image(self.icon.winfo_width() / 2,
            self.icon.winfo_height() / 2, anchor='center', image=img)
        self.icon.image = img

        # update high and low temps
        self.label_temps['text'] = \
            f"{round(res['temp']['max'])}° / {round(res['temp']['min'])}°"