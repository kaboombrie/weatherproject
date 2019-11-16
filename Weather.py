# Brie Prater
# CIS 245
# Final Project Draft

import requests # this imports the requests library
from pprint import pprint
headers = {
    'cache-control': "no-cache",
}
city = ''
def weatherforecast(): # this is the main function
    city = input(print("Please enter your city or zipcode: ")) # this asks for user to input city
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=ac6c956f0465b1149196bd54dd344fbe&units=imperial'.format(city)
    try:
        res = requests.get(url) # this uses the url to connect to the API
        data = res.json()
        temp = data['main']['temp']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description']
        print("The weather in " + city + " is:") 
        print('Temperature : {} degrees fahrenheit'.format(temp)) # this displays the weather information in a legible format
        print('Wind Speed : {} mph'.format(wind_speed))
        print('Description : {}'.format(str.title(description)))
    except requests.ConnectionError:
        print("Could not connect to server. Please try again.") # this informs the user that connection was unsuccessful

def menu(): 
    while True:
        print("Would you like check another city?")
        again = input("Enter y to continue or n to exit.")
        if again == 'y': # checks user input 
            weatherforecast()
        elif again == 'n': # checks user input
            print("Thanks for using our service!")
            break
        else: # if neither of the acceptable inputs, return error 
            print("That response is invalid. Please try again.")
            continue

print("Welcome to the Weather Forecast!")
weatherforecast() # this calls the main function 
menu() # this allows the user to run the program multiple times


