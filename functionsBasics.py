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
    #print(f"Total price is {total_price}")
    return total_price  # Return the calculated total price

TotalP = price_calculater(30)
print(TotalP)  # This will print the returned value
if TotalP > 90:
    print("Price is High.")
elif TotalP <= 50:
    print("Price is Low.")
else:
    print("Price is Moderate.")


#Returning from Lists

def NumbersList():
    numbers = [1, 2, 3, 4, 5]
    first_number = numbers[0]
    last_number = numbers[-1]
    return first_number, last_number  # Return both values as a tuple

first, last = NumbersList()
print(first)  # This will print the first number
print(last)   # This will print the last number
print(f"First number: {first}, Last number: {last}") # This will print both numbers in a formatted string


#Function with variable length arguments

def variable_length_args(num1, *num2):
    print(num1)

    sum = num1
    for i in num2:
        sum += i
    return sum
print(variable_length_args(4,4,4,5))

#function wit keyword large arguments
def keywordlarge(name, **kwlargeargs):
    print(f"Name : {name}")

    for k,v in kwlargeargs.items():
        print(f"{k} : {v}")

keywordlarge(name = 'Kiran', age = 45, Loc = 'Sydney')