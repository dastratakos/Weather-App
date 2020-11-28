from datetime import datetime

from PIL import Image, ImageTk
import tkinter as tk

from src.styles import *

class Day(tk.Frame):
    def __init__(self, parent, index, dark_mode):
        tk.Frame.__init__(self, parent)

        self.dark_mode = dark_mode
        self.icon_name = None

        self.root = tk.Frame(parent)
        self.root.place(relx=(0.125 * index), y=0, relwidth=0.125, relheight=1)

        self.l_date = tk.Label(self.root, font=(FONT, 15), anchor='n')
        self.l_date.place(relx=0, rely=0, relwidth=1, height=20)

        self.icon = tk.Canvas(self.root, bd=0, highlightthickness=0)
        self.icon.place(relx=0, rely=0.5, relwidth=1, height=ICON_SIZE, anchor='w')

        self.l_temps = tk.Label(self.root, font=(FONT, 15), anchor='n')
        self.l_temps.place(relx=0.5, rely=1, relwidth=1, height=20, anchor='s')

        self.updateMode(dark_mode)

    def format(self, res):
        """
        Args:
            res (dict): sub-response that contains information for a single day
        """
        # update date
        self.l_date['text'] = datetime.fromtimestamp(res['dt']).strftime('%a %-d')

        # open image
        self.icon_name = res['weather'][0]['icon']
        self.loadIcon()

        # update high and low temps
        self.l_temps['text'] = \
            f"{round(res['temp']['max'])}° / {round(res['temp']['min'])}°"

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

        self.l_date['fg'] = COLOR_DARK_TEXT_QUATERNARY if dark_mode else COLOR_TEXT_QUATERNARY
        self.l_date['bg'] = COLOR_DARK_MAIN if dark_mode else COLOR_MAIN

        self.icon['bg'] = COLOR_DARK_MAIN if dark_mode else COLOR_MAIN

        self.l_temps['fg'] = COLOR_DARK_TEXT_PRIMARY if dark_mode else COLOR_TEXT_PRIMARY
        self.l_temps['bg'] = COLOR_DARK_MAIN if dark_mode else COLOR_MAIN

        self.loadIcon()