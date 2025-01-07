# All Libraries Installed :- 
import requests
import os

# API Key Used :- 
api_key = "" # {Enter your own API key }
base_url = "http://api.openweathermap.org/data/2.5/weather?"


# Displaying The Visual Interface :- 
print("WEATHER INFORMATION 🌦️ ")
city_name = input("Enter city name: ")
print("What Do You Want to Know :- ")
print("1. Temperature 🌡️")
print("2. Pressure 📏 ")
print("3. Wind Speed 💨 ")
print("4. Humidity 💧")
print("5. All of the Above 📋")
print("6. Exit ")
choice = int(input("Please let us know :- "))

# Construct the complete URL :- 
complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"

# Get the response from the API :-  
response = requests.get(complete_url)

# Convert the response to JSON format :- 
data = response.json()


# Check If The City Is Found Or Not :- 
if data["cod"] == "404":
    print("City not found!")
else:
    main_data = data["main"]
    weather_data = data["weather"][0]
    wind_data = data["wind"]

# For Actually Showing The Data :- 
if choice == 1:
    print("Temperature in ",city_name,"is:- ",main_data['temp'],"°C")
    print("Description for ",city_name,"is:- ",main_data['description'],".")
    print("Thank You For using us . Hope you Have a Nice Day..")

elif choice == 2:
    print("Pressure in ",city_name,"is:- ",main_data['pressure'],"hPa")
    print("Description for ",city_name,"is:- ",main_data['description'],".")
    print("Thank You For using us . Hope you Have a Nice Day..")

elif choice == 3:
    print("Humidity in ",city_name,"is:- ",main_data['humidity'],"%")
    print("Description for ",city_name,"is:- ",main_data['description'],".")
    print("Thank You For using us . Hope you Have a Nice Day..")

elif choice == 4:
    print("Wind Speed In ",city_name,"is:- ",main_data['speed'],"m/s")
    print("Description for ",city_name,"is:- ",main_data['description'],".")
    print("Thank You For using us . Hope you Have a Nice Day..")

elif choice == 5:
    print("Temperature in ",city_name,"is:- ",main_data['temp'],"°C")
    print("Pressure in ",city_name,"is:- ",main_data['pressure'],"hPa")
    print("Humidity in ",city_name,"is:- ",main_data['humidity'],"%")
    print("Wind Speed in ",city_name,"is:- ",wind_data['speed'],"m/s")
    print("Describing the weather in one word for ",city_name,"is:- ",weather_data['description'],".")
    print("Thank You For using us . Hope you Have a Nice Day..")

elif choice == 6:
    print("Exiting The Weather API .. ")
    print("Thank You for giving us the opportunity to serve you . ")
    os._exit(0)
    
else:
    print("We Are Sorry to help you with that input . ")
    print("PLease write your query on raunakjain1002@gmail.com")
    print("Hope you Have a Nice Day . Thank You! 😊")

    
