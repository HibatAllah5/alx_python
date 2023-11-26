#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(repr(number)[-1])

if number < 0:
    print("last digit of", number, "is", last_digit*-1 , "and is less than 6 and not 0")
elif last_digit > 5:
    print("Last digit of", number, "is", last_digit, "and is greater than 5")
elif last_digit < 6:
    print("last digit of", number, "is", last_digit, "and is less than 6 and not 0")
else:
    print("last digit of", number, "is", last_digit, "and is 0")
