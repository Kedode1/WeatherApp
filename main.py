import datetime
import requests

def recommend_clothing(temperature, status):
    if status == "clear sky":
        if temperature > 30:
            return "Wear light and breathable clothing, sunglasses, and a hat."
        elif temperature > 20:
            return "Opt for shorts, a t-shirt, and sunscreen."
        elif temperature > 10:
            return "Wear a light jacket or sweater."
        else:
            return "Bundle up with a warm coat, gloves, and a scarf."

    elif status == "cloudy":
        if temperature > 25:
            return "A light sweater or long-sleeve shirt would be comfortable."
        elif temperature > 15:
            return "A hoodie or light jacket is recommended."
        else:
            return "Wear a warmer jacket or coat."

    elif status == "rainy":
        if temperature > 20:
            return "A waterproof jacket and an umbrella would be useful."
        elif temperature > 10:
            return "Wear a raincoat or waterproof layer."
        else:
            return "Dress warmly with a waterproof jacket and rain boots."

    else:
        return "Sorry, I don't have specific recommendations for that weather status."

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
API_KEY = '11239066031546d8617bdf0a767e4ba3'
city = input("Enter the name of your city: ")

URL = BASE_URL + 'appid=' + API_KEY + '&q=' + city
response = requests.get(URL).json()

temp_k = response['main']['temp']
description = response['weather'][0]['description']
temp_c = round(temp_k-273.15,2)
print(temp_c,'Degrees Celsius')
print(description)
temperature = temp_c

recommendation = recommend_clothing(temperature, description)
print("Temperature: ",temp_c,'Degrees')
print("Weather status: ", description)
print("Recommendation:", recommendation)