import json

import tkinter as tk

from src.styles import *

class SearchModule(tk.Frame):
    def __init__(self, parent, controller, dark_mode):
        tk.Frame.__init__(self, parent)

        with open('./open-weather-app/city.list.json') as f:
            self.city_list = json.load(f)

        self.root = tk.Frame(parent, bd=10)
        self.root.place(relx=0.5, rely=0.05, relwidth=0.85, relheight=0.2, anchor='n')

        self.l_city = tk.Label(self.root, text='City:', font=(FONT, 20),
            anchor='e')
        self.l_city.place(rely=0, relx=0.1, relwidth=0.2, height=35, anchor='n')
        self.e_city = tk.Entry(self.root, text='Saratoga', font=(FONT, 20))
        self.e_city.place(rely=0, relx=0.5, relwidth=0.5, height=35, anchor='n')

        self.l_state = tk.Label(self.root, text='State:', font=(FONT, 20),
            anchor='e')
        self.l_state.place(rely=0.5, relwidth=0.2, height=35, anchor='w')
        self.e_state = tk.Entry(self.root, text='CA', font=(FONT, 20))
        self.e_state.place(rely=0.5, relx=0.25, relwidth=0.5, height=35, anchor='w')

        self.l_country = tk.Label(self.root, text='Country:', font=(FONT, 20),
            anchor='e')
        self.l_country.place(rely=1, relx=0.1, relwidth=0.2, height=35, anchor='s')
        self.e_country = tk.Entry(self.root, text='USA', font=(FONT, 20))
        self.e_country.place(rely=1, relx=0.5, relwidth=0.5, height=35, anchor='s')

        self.b_search = tk.Button(self.root, text='SEARCH', font=(FONT, 20, 'bold'),
            highlightthickness=0,
            command=lambda: controller.buttonSearchPressed(
                self.e_city.get(),
                self.e_state.get(),
                self.e_country.get()))
        self.b_search.place(relx=0.8, rely=0.3, relwidth=0.2, relheight=0.4)

        self.updateMode(dark_mode)
    
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

    def updateMode(self, dark_mode):
        self.root['bg'] = COLOR_DARK_BACKGROUND if dark_mode else COLOR_BACKGROUND

        self.b_search['fg'] = COLOR_DARK_BACKGROUND if dark_mode else COLOR_BACKGROUND
        self.b_search['highlightbackground'] = COLOR_DARK_BUTTON if dark_mode else COLOR_BUTTON
        self.b_search['activebackground'] = COLOR_DARK_BUTTON if dark_mode else COLOR_BUTTON

        labels = [self.l_city, self.l_state, self.l_country]
        entries = [self.e_city, self.e_state, self.e_country]

        for label, entry in zip(labels, entries):
            label['fg'] = COLOR_DARK_TEXT_TERTIARY  if dark_mode else COLOR_TEXT_TERTIARY
            label['bg'] = COLOR_DARK_BACKGROUND     if dark_mode else COLOR_BACKGROUND
            entry['fg'] = COLOR_DARK_TEXT_SECONDARY if dark_mode else COLOR_TEXT_SECONDARY
            entry['bg'] = COLOR_DARK_MAIN           if dark_mode else COLOR_MAIN
            entry['insertbackground'] = COLOR_DARK_TEXT_SECONDARY if dark_mode else COLOR_TEXT_SECONDARY
            entry.config(
                highlightbackground = COLOR_DARK_TEXT_SECONDARY if dark_mode else COLOR_MAIN,
                highlightcolor      = COLOR_DARK_TEXT_SECONDARY if dark_mode else COLOR_MAIN)