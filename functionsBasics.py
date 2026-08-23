#Functions

def check_weather():
    temp = 22
    if temp > 25:
        print("It's a hot day")
    elif temp < 10:
        print("It's cold day")
    else:
        print("It's a lovely day")

check_weather()

#function with parameters

def check_weather(temp):
    if temp > 25:
        print("It's a hot day")
    elif temp < 10:
        print("It's cold day")
    else:
        print("It's a lovely day")

check_weather(33)