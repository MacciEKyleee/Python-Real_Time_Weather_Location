# Author | Maciej Cieszyński
# Encoding | -UTF-8- #

import requests
import os
from datetime import datetime


user_api = os.environ['current_weather_data']
#ity_name = ['Warsaw', 'Cracow', 'Lodz', 'Wrocław', 'Poznań', 'Gdańsk', 'Szczecin', 'Bydgoszcz']
#location = input(f'Chose the city name {city_name} : ')
print("")
location = input(f'Enter the name of the city: ')
# chosen_datetime = input('Select a weather measurement date or enter "null":')

Full_API_link = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + user_api
#print(Full_API_link)

api_link = requests.get(Full_API_link)
api_data = api_link.json()

if api_data['cod'] == '404':
    print('Invalid Name of City: {} -> Please write correct City name'.format(location))
else:
    # if chosen_datetime == 'null':
    #     current_date_time = datetime.now().strftime('%d %b %Y | %I:%M:%S %p')
    # else:
    #     current_date_time = datetime.now().strftime('%d %b %Y | %I:%M:%S %p')

    current_date_time = datetime.now().strftime('%d %b %Y | %I:%M:%S %p')
    city_temperature = ((api_data['main']['temp'])-273.15)
    weather_desc = api_data['weather'][0]['description']
    humidity = api_data['main']['humidity']
    wind_speed = api_data['wind']['speed']
    country = api_data['sys']['country']

    print("------------------------------------------------------------------------")
    print('Weather Stats for - {} || {}'.format(location.upper(), current_date_time))
    print("------------------------------------------------------------------------")

    print('City                         :', location)
    print('Country (abbreviation)       :', country)
    print('Current temperature is       : {:.2f} deg C'.format(city_temperature))
    print('Current weather description  :', weather_desc)
    print('Current humidity is          :', humidity, '%')
    print('Current speed of wind is     :', wind_speed, 'km/h')
    print("------------------------------------------------------------------------")


# if __name__=='main':
