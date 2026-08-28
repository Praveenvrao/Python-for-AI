import math as M 

def multiple(a, b):
    return a * b

def addition(a, b):
    return a + b

Multiplication = multiple(5, 10)
Addition = addition(5, 10)
print(f"Multiplication of 5 & 10 is : {Multiplication}")
print(f"Addition of 5 & 10 is : {Addition}")

from math import ceil, floor

def roundup(value):
    return ceil(value)
def rounddown(value):
    return floor(value)

print(f"Roundup of 5.2 is : {roundup(5.2)}")
print(f"Rounddown of 5.2 is : {rounddown(5.2)}")


#Swapping two numbers
def swap(a, b):
    a = 5
    b = 10
    print(f"Before swapping: a = {a}, b = {b}")
    a = a+b
    b = a-b
    a = a-b
    print(f"After swapping: a = {a}, b = {b}")
    return a, b

print(swap(5, 10))

def simpleswap(a, b):
    print(f"Before swapping : a = {a}, b = {b}")
    a,b = b,a
    print(f"After swapping : a = {a}, b = {b}")
    return a, b

print(simpleswap(5, 10))