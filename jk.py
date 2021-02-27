import requests
from tkinter import *
from tkinter import Button
from tkinter import Label


def weather():
    city = city_list_box.get()
    url = "https://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22".format(city)
    res = requests.get(url)
    output = res.json()

    weather_Condition = output['weather'][0]['description']
    temperature = output['main']['temperature']
    humidity = output['main']['humidity']
    wind_speed = output['wind']['speed']

    weather_condition_label.configure(text="Weather Status: " + weather_Condition)
    temperature_label.configure(text="Weather Status: " + str(temperature))
    humidity_label.configure(text="Humidity: " + str(humidity))
    wind_speed_label.configure(text="Wind Speed: " + str(wind_speed))


window: Tk = Tk()
window.geometry("400x350")
x_dy = str.upper("MyBot")
x_tf = window.title(x_dy)

city_list_name = ["Nairobi", "Mombasa", "Delhi", "Washington DC", "Ohio", "Guatemala"]
city_list_box = StringVar(window)
city_list_box.set("Select Your City:")
option = OptionMenu(window, city_list_box, *city_list_name)
option.grid(row=2, column=2, padx=150, pady=10)

b_x = Button(window, text="RUN", fg="green", width=15, command=weather)
b_x.grid(row=5, column=2, padx=150, pady=0)

weather_condition_label = Label(window, font=("times", 12, 'bold'))
weather_condition_label.grid(row=10, column=2)

temperature_label = Label(window, font=("times", 12, 'bold'))
temperature_label.grid(row=12, column=2)

humidity_label = Label(window, font=("times", 12, 'bold'))
humidity_label.grid(row=14, column=2)

wind_speed_label = Label(window, font=("times", 12, 'bold'))
wind_speed_label.grid(row=16, column=2)


if __name__ == '__main__':
    window.mainloop()
