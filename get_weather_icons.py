import os
import urllib.request

def downloadIcons(base_url, file_names, output_dir):
	os.makedirs(output_dir, exist_ok=True)
	for file in file_names:
		# if not os.path.exists(base_url + file):
		urllib.request.urlretrieve(base_url + file, output_dir + file)

def main(get_google=True):
	if get_google:
		base_url = 'http://www.gstatic.com/images/icons/material/apps/weather/2x/'
		file_names = [
			'wintry_mix_rain_snow_light_color_96dp.png',
			'haze_fog_dust_smoke_light_color_96dp.png',
			'cloudy_light_color_96dp.png',
			'snow_showers_snow_light_color_96dp.png',
			'flurries_light_color_96dp.png',
			'drizzle_light_color_96dp.png',
			'showers_rain_light_color_96dp.png',
			'heavy_rain_light_color_96dp.png',
			'strong_tstorms_light_color_96dp.png',
			'isolated_scattered_tstorms_day_light_color_96dp.png',
			'isolated_scattered_tstorms_night_light_color_96dp.png',
			'scattered_showers_day_light_color_96dp.png',
			'scattered_showers_night_light_color_96dp.png',
			'partly_cloudy_light_color_96dp.png',
			'partly_cloudy_night_light_color_96dp.png',
			'mostly_sunny_light_color_96dp.png',
			'mostly_clear_night_light_color_96dp.png',
			'mostly_cloudy_day_light_color_96dp.png',
			'mostly_cloudy_night_light_color_96dp.png',
			'sunny_light_color_96dp.png',
			'clear_night_light_color_96dp.png'
		]
		output_dir = './res/google_icons/'
	else:
		base_url = 'https://openweathermap.org/img/w/'
		file_names = ['01d.png', '02d.png', '03d.png', '04d.png', '09d.png',
			'10d.png', '11d.png', '13n.png', '50d.png', '01n.png', '02n.png',
			'03n.png', '04n.png', '09n.png', '10n.png', '11n.png', '13n.png',
			'50n.png']
		output_dir = './res/open_weather_icons/'

	downloadIcons(base_url, file_names, output_dir)

if __name__=='__main__':
	main()