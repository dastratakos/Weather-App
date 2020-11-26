import json

import tkinter as tk

from src.styles import *

class SearchModule(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        with open('./open-weather-app/city.list.json') as f:
            self.city_list = json.load(f)

        self.root = tk.Frame(parent, bg=COLOR_BLUE, bd=10)
        self.root.place(relx=0.5, rely=0.05, relwidth=0.85, relheight=0.2, anchor='n')

        self.label_city = tk.Label(self.root, text='City:', font=(FONT, 20),
            anchor='e', bg=COLOR_BLUE, fg=COLOR_WHITE)
        self.label_city.place(rely=0, relwidth=0.2, height=35)
        self.entry_city = tk.Entry(self.root, text='Saratoga', font=(FONT, 20),
            fg=COLOR_DARK_GRAY)
        self.entry_city.place(rely=0, relx=0.25, relwidth=0.5, height=35)

        self.label_state = tk.Label(self.root, text='State:', font=(FONT, 20),
            anchor='e', bg=COLOR_BLUE, fg=COLOR_WHITE)
        self.label_state.place(rely=0.3333, relwidth=0.2, height=35)
        self.entry_state = tk.Entry(self.root, text='CA', font=(FONT, 20),
            fg=COLOR_DARK_GRAY)
        self.entry_state.place(rely=0.3333, relx=0.25, relwidth=0.5, height=35)

        self.label_country = tk.Label(self.root, text='Country:', font=(FONT, 20),
            anchor='e', bg=COLOR_BLUE, fg=COLOR_WHITE)
        self.label_country.place(rely=0.6666, relwidth=0.2, height=35)
        self.entry_country = tk.Entry(self.root, text='USA', font=(FONT, 20),
            fg=COLOR_DARK_GRAY)
        self.entry_country.place(rely=0.6666, relx=0.25, relwidth=0.5, height=35)

        self.button_go = tk.Button(self.root, text='GO', fg=COLOR_GREEN,
            font=(FONT, 20, 'bold'), 
            command=lambda: controller.buttonPressed(self.entry_city.get(),
                self.entry_state.get(), self.entry_country.get()))
        self.button_go.place(relx=0.8, rely=0.3, relwidth=0.2, relheight=0.4)
    
    def getCity(self, city_name, state_code, country_code):
        results = [x for x in self.city_list
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