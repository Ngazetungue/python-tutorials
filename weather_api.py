# import module
import requests, json

# Enter your API key here
api_key = 'Enter your API key'
 
# store weather url in variable called weather_data
weather_data = "http://api.openweathermap.org/data/2.5/weather?"
 
# Get city name from the user input
my_input = input("Enter city name : ")
 
weather_url = weather_data + "appid=" + api_key + "&q=" + my_input
 
# Get requests module and return response object
response = requests.get(weather_url)
 
# convert json format data into python format data
result = response.json()
 
if result["cod"] != "404":
    list_of_data = result["main"]
    current_pressure = list_of_data["pressure"]
    current_humidity = list_of_data["humidity"]
    weather = result["weather"]
    weather_description = weather[0]["description"]
 
    print(" atmospheric pressure: " +
                    str(current_pressure) +
          "\n humidity : " +
                    str(current_humidity)  +
          "\n description : " +
                    str(weather_description))
 
else:
    print(" City Not Found ")