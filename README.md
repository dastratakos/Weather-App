I used this command to create an executable:
```
pyinstaller --onefile --icon=Weather.ico weather_app.py
```

TODO:
- [ ] light vs. dark theme for day and night (or user-controlled)
- [ ] scroll to more hours
- [ ] ability to click on different days and update info
- [x] move code to `src` file
- [ ] create executable
- [x] clean up get_weather_icons.py
- [ ] check line wrapping, pick order for (text=, fg=, font=, ...) for TK components
- [ ] Rename files
- [ ] If there are multiple search results, display them