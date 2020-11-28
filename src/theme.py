from PIL import Image, ImageTk
import tkinter as tk

from src.styles import *

SIZE = 20

class Theme(tk.Frame):
    def __init__(self, parent, controller, dark_mode):
        tk.Frame.__init__(self, parent)

        self.dark_mode_icon = self.makeIcon('./res/dark_mode.png', COLOR_MAIN)
        self.light_mode_icon = self.makeIcon('./res/light_mode.png', COLOR_DARK_MAIN)

        self.b_theme = tk.Button(parent, bd=0,
            image=self.light_mode_icon if dark_mode else self.dark_mode_icon,
            command=lambda: controller.buttonThemePressed())
        self.b_theme.place(relx=0.99, rely=0.01, anchor='ne')

    def makeIcon(self, filename, background):
        raw_icon = (Image.open(filename).convert('RGBA').resize((SIZE, SIZE)))
        background = Image.new('RGB', raw_icon.size, background)
        background.paste(raw_icon, None, raw_icon)
        return ImageTk.PhotoImage(background)

    def updateMode(self, dark_mode):
        self.b_theme['image'] = self.light_mode_icon if dark_mode else self.dark_mode_icon
        self.b_theme['highlightbackground'] = COLOR_DARK_MAIN if dark_mode else COLOR_MAIN
        self.b_theme['activebackground'] = COLOR_DARK_MAIN if dark_mode else COLOR_MAIN