import requests

api_key = 'MY API KEY'

my_input = input("Enter city Name: ")

weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid={api_key}')

print(weather_data.json())