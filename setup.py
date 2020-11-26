from setuptools import setup, find_packages

setup(
    name='WeatherApp',
    description='Weather App',
    author='Dean Stratakos',
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'tkinter',
    ]
)