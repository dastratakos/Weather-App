from PIL import Image, ImageTk
import tkinter as tk

from src.styles import *

SIZE = 20

class Theme(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.dark_mode_img = ImageTk.PhotoImage(Image.open('./res/dark_mode.png')
                                                     .resize((SIZE, SIZE)))
        self.light_mode_img = ImageTk.PhotoImage(Image.open('./res/light_mode.png')
                                                      .resize((SIZE, SIZE)))

        self.button_theme = tk.Button(parent, image=self.dark_mode_img, bd=0,
            command=lambda: controller.buttonThemePressed())
        self.button_theme.place(relx=0.99, rely=0.01, anchor='ne')

    def updateMode(self, darkTheme):
        self.button_theme['image'] = self.light_mode_img if darkTheme else self.dark_mode_img