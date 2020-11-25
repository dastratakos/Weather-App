import os
import requests
import urllib.request

files = """
http://www.gstatic.com/images/icons/material/apps/weather/2x/wintry_mix_rain_snow_light_color_96dp.png

http://www.gstatic.com/images/icons/material/apps/weather/2x/haze_fog_dust_smoke_light_color_96dp.png

http://www.gstatic.com/images/icons/material/apps/weather/2x/cloudy_light_color_96dp.png

http://www.gstatic.com/images/icons/material/apps/weather/2x/snow_showers_snow_light_color_96dp.png

http://www.gstatic.com/images/icons/material/apps/weather/2x/flurries_light_color_96dp.png

http://www.gstatic.com/images/icons/material/apps/weather/2x/drizzle_light_color_96dp.png

http://www.gstatic.com/images/icons/material/apps/weather/2x/showers_rain_light_color_96dp.png

http://www.gstatic.com/images/icons/material/apps/weather/2x/heavy_rain_light_color_96dp.png

http://www.gstatic.com/images/icons/material/apps/weather/2x/strong_tstorms_light_color_96dp.png

http://www.gstatic.com/images/icons/material/apps/weather/2x/isolated_scattered_tstorms_day_light_color_96dp.png

http://www.gstatic.com/images/icons/material/apps/weather/2x/isolated_scattered_tstorms_night_light_color_96dp.png

http://www.gstatic.com/images/icons/material/apps/weather/2x/scattered_showers_day_light_color_96dp.png

http://www.gstatic.com/images/icons/material/apps/weather/2x/scattered_showers_night_light_color_96dp.png

http://www.gstatic.com/images/icons/material/apps/weather/2x/partly_cloudy_light_color_96dp.png

http://www.gstatic.com/images/icons/material/apps/weather/2x/partly_cloudy_night_light_color_96dp.png

http://www.gstatic.com/images/icons/material/apps/weather/2x/mostly_sunny_light_color_96dp.png

http://www.gstatic.com/images/icons/material/apps/weather/2x/mostly_clear_night_light_color_96dp.png

http://www.gstatic.com/images/icons/material/apps/weather/2x/mostly_cloudy_day_light_color_96dp.png

http://www.gstatic.com/images/icons/material/apps/weather/2x/mostly_cloudy_night_light_color_96dp.png

http://www.gstatic.com/images/icons/material/apps/weather/2x/sunny_light_color_96dp.png

http://www.gstatic.com/images/icons/material/apps/weather/2x/clear_night_light_color_96dp.png
"""

img_dir = './google_icons/'
if not os.path.exists(img_dir):
	os.makedirs(img_dir)
name = 1
for file in files.split():
	urllib.request.urlretrieve(file, f'{name}.png')
	# res = requests.get(file)
	# print(type(res))
	# print(res)
	name += 1

# day = ['01d.png', '02d.png', '03d.png', '04d.png', '09d.png', '10d.png', '11d.png', '13n.png', '50d.png']
# night = ['01n.png', '02n.png', '03n.png', '04n.png', '09n.png', '10n.png', '11n.png', '13n.png', '50n.png']

# base_url = 'https://openweathermap.org/img/w/'
# img_dir = './icons/'
# if not os.path.exists(img_dir):
# 	os.makedirs(img_dir)

# Get the day weather icons
# for name in day:
# 	file_name = img_dir + name
# 	if not os.path.exists(file_name):
# 		urllib.request.urlretrieve(base_url + name, file_name)

# # Repeat the same thing for night weather icons
# for name in night:
# 	file_name = img_dir + name
# 	if not os.path.exists(file_name):
# 		urllib.request.urlretrieve(base_url + name, file_name)
