import sys
from tkinter import *
import json
import requests
import time

root = Tk()
root.title("weather app")
root.geometry("500x250")
root.configure(background="#9efea3")

with open("city_list.json", "r", encoding="utf-8") as city:
    data = json.load(city)

jj = Entry(root, width=30)
jj.grid(row=0, column=1, pady=10)

jj_label= Label(root, text="city: ")
jj_label.grid(row=0, column=0, pady=10, padx=5)

def search():
    global city_list
    global jj_city

    jj_city = jj.get()
    city_list = []
    n = 0
    city_string = ""

    for code in data:
        if jj_city.capitalize() in code["name"]:
            city_string += str(n) + " " + code["name"] + " " + code["country"] + " " + str(code["id"]) + "\n"
            city_list.append(code["id"])
            n += 1
            city_label.config(text=city_string)


#search button
search_btn = Button(root, text="Search", bg="red", fg="white", command=search)
search_btn.grid(row=0, column=3, pady=10, padx=5)

#fetching the weather data
fetch_label = Label(root, text="input city number")
fetch_label.grid(row=2, column=0, pady=10, padx=10)

fetch_entry = Entry(root, width=30)
fetch_entry.grid(row=2, column=1, padx=10, pady=10)
def fetch():
    global city_list
    global jj1
    global jj_city

    jj1 = int(fetch_entry.get())

    display = Tk()
    display.title("weather app")
    display.geometry("400x280")

    #fetching weather data
    try:
        api_request = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?id={city_list[jj1]}&appid=ff134e134fe1f7cf2de0195f54d7f964&units=metric")
        api = json.loads(api_request.content)
        temp = api["main"]["temp"]
        temp_feel = api["main"]["feels_like"]
        weather = api["weather"][0]["main"]
        sunset = api["sys"]["sunset"]
    except:
        api = "error..."
        sys.exit("Error occured")

    # creating label font
    font_tuple = ("verdana", 12, "normal")

    # setting the background
    # adding image file
    if weather == "Rain":
        display.configure(background="#1E90FF")
    elif weather == "Clear":
        display.configure(background="#87CEEB")
    elif weather == "Clouds":
        display.configure(background="#696969")
    elif weather == "Snow":
        display.configure(background="FFFFFF")
    elif weather == "Drizzle":
        display.configure(background="ADD8E6")
    elif weather == "Thunderstorm":
        display.configure(background="2F4F4F")
    else:
        display.configure(background="#7f7d79")

    # creating labels
    mylabel = Label(display, text="temperature: " + str(temp) + chr(176) + "C", font=font_tuple)
    mylabel.grid(row=1, column=0, sticky="w", padx=10, pady=30)
    mylabel1 = Label(display, text="Feels like " + str(temp_feel) + chr(176) + "C", font=font_tuple)
    mylabel1.grid(row=2, column=0, sticky="sw", padx=10, pady=10)
    mylabel2 = Label(display, text="weather: " + str(weather), font=("verdana", 14, "normal"))
    mylabel2.grid(row=0, column=1, sticky="n", columnspan=2, pady=10)
    # seeting sunset time
    tt = time.ctime(sunset)
    mylabel3 = Label(display, text="Sun set\n" + tt[11:16], font=font_tuple)
    mylabel3.grid(row=1, column=1, sticky="e", padx=10, pady=30)
    mylabel4 = Label(display, text=jj_city)
    mylabel4.grid(row=0, column=0, sticky="nw", padx=10, pady=10)




fetch_btn = Button(root, text="Fetch", bg="red", fg="white", command=fetch)
fetch_btn.grid(row=2, column=2, padx=5, pady=5)

city_label = Label(root, text="")
city_label.grid(row=1, column=0, columnspan=3, padx=20)

'''
try:
    api_request = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?id=1805298&appid=ff134e134fe1f7cf2de0195f54d7f964&units=metric")
    api = json.loads(api_request.content)
    temp = api["main"]["temp"]
    temp_feel = api["main"]["feels_like"]
    weather = api["weather"][0]["main"]
    sunset = api["sys"]["sunset"]
except:
    api = "error..."
    sys.exit("Error occured")


'''

root.mainloop()
