#task1
#Download and save to file robots.txt from wikipedia, twitter websites etc.
from urllib import request

import requests as requests

remote_url = 'https://en.wikipedia.org/robots.txt'

local_file = 'local_copy.txt'

request.urlretrieve(remote_url, local_file)
#task2
# Load data
# Download all comments from a subreddit of your choice using
# URL: https://api.pushshift.io/reddit/comment/search/ .
# As a result, store all comments in chronological order in JSON and dump it to a file.

s = requests.get('https://api.pushshift.io/reddit/comment/search/')
#json_file = 'local_copy.json'
dat_s = s.json()
print(dat_s)
d = dat_s.get('data')

print(d)


# with open("data_file.json", "w") as write_file:
#     json.dump(d, write_file)





# task3
# The Weather app
# Write a console application which takes as an input a city name and returns
# current weather in the format of your choice.
# For the current task, you can choose any weather API or website or use
# https://openweathermap.org

import requests

api_key = "4836b8877b4d8c5165fc81257d2e5941"

def weather_app():
    city = input("Ведіть своє місто: ")
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")
    print(f"Розташування: {data.json().get('name')}, {data.json().get('sys').get('country')}")
    print(f"Температура: {data.json().get('main')['temp']}°C")
    print(f"Вологість: {data.json().get('main')['humidity']}%")
    print(f"Швидкість  вітру: {data.json().get('wind')['speed']} km/h")
    return weather_app
w = weather_app()
