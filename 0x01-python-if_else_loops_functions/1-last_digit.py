#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

if number > 0:
    ldigit = number % 10
elif number < 0:
    ldigit = (number * -1) % 10
    ldigit *= -1
else:
    ldigit = 0

print(f"Last digit of {number} is {ldigit} and is", end=' ')

if ldigit > 5:
    print("greater than 5")
elif ldigit < 6 and ldigit != 0:
    print("less than 6 and not 0")
else:
    print("0")
