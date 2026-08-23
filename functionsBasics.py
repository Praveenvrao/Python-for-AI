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

#function with parameters with Local variables

def check_weather(temp, season):
    if temp > 25:
        print(f"It's a hot day and it's {season} season")
    elif temp < 10:
        print(f"It's cold day and it's {season} season")
    else:
        print(f"It's a lovely day and it's {season} season")

check_weather(season = "Winter", temp = 1)

def check_weather(temp, season = "Summer"):
    if temp > 25:
        print(f"It's a hot day and it's {season} season")
    elif temp < 10:
        print(f"It's cold day and it's {season} season")
    else:
        print(f"It's a lovely day and it's {season} season")

check_weather(temp = 1)

#function with global variables

taxrate = 0.20  # Global variable
discount = 25  # Global variable
def price_calculater(price):
    total_price = price + ((price * taxrate) - discount)
    print(f"Total price is {total_price}")

price_calculater(100)

