# Tkinter used to build GUI
from tkinter import *
from tkinter import Label
from tkinter import Button
import requests

# Create a function that will help extract,open, read,and display the current weather condition from servers

def weather():
    # This city variable will extract the name of the city input by the user from the city list box.
    city = city_listbox.get()
    """
    # Openweather API recommends calling API by city id to avoid ambiguous results which will be unfriendly to the end user
    # api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
    """
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=PASTE YOUR openweathermap API ID HERE".format(city)

    # a request function that will get the data from the above url
    res = requests.get(url)
    # we are now converting this data into .json format to be output
    output = res.json()
    # Go to the weather data and inspect it.since it is quite big, decide which one to display to the user

    weather_condition = output['weather'][0]['description']
    # Under the weather key, at the 0th index, under the key description"""
    # lets now create for all
    temperature = output['main']['temp']
    humidity = output['main']['humidity']
    wind_speed = output['wind']['speed']

    # Inserting text to our labels we now configure our GUI
    weather_condition_label.config(text="Weather Condition : " + weather_condition)
    temp_condition_label.config(text="Temperature : " + str(temperature))  # Must be type casted into str
    humidity_condition_label.config(text="Humidity : " + str(humidity))
    wind_speed_condition_label.config(text="Wind Speed : " + str(wind_speed))

    # End of extraction of the data from our json

# create a tkinter window


window: Tk = Tk()
# Let's define the geometry of our Tk()
bot_title = "My Small weather Bot"
var_t = window.title(bot_title)
var = window.geometry("400x350")

# "creating a variable list[] where all the city names will be stored as in JSON
city_names_list = ["Delhi", "Nairobi", "Mombasa", "Nakuru", "Kisumu", "Eldoret", 
                "Cairo", "Larkana","Kyoto", "Tokyo", "Matsue", "Yokohama", "Kericho"]

"""
Since this is a string variable(City_name_list)
"""

city_listbox = StringVar(window)
# We are now telling our Tkinter window to enable us to toggle btn the cities to choose from
city_listbox.set("Select the city")

# For the list box to show up, we need to declare another variable that gives us that option and takes
# the window parameters as below:
option = OptionMenu(window, city_listbox, *city_names_list)
# we are now showing these variables/options in our tkinter window as in grid format

option.grid(row=2, column=2, padx=150, pady=10)
# Now lets create our select button
b1 = Button(window, text="RUN", fg="green", width=15, command=weather)

# Command is the action triggered which is our weather()
# create a grid of boxes
b1.grid(row=5, column=2, padx=150, pady=0)
# Create your labels of our window for display for the user GUI

weather_condition_label = Label(window, font=('times', 10, 'bold'))
weather_condition_label.grid(row=10, column=2)

temp_condition_label = Label(window, font=('times', 10, 'bold'))
temp_condition_label.grid(row=12, column=2)

humidity_condition_label: Label = Label(window, font=('times', 10, 'bold'))
humidity_condition_label.grid(row=14, column=2)

wind_speed_condition_label = Label(window, font=('times', 10, 'bold'))
wind_speed_condition_label.grid(row=16, column=2)


if __name__ == '__main__':
    window.mainloop()
