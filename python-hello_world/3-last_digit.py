import random
number = random.randint(-10000, 10000)
Last_digit = int(repr(number)[-1])
if number < 0:
    print("Last digit of", number, "is", Last_digit*-1 , "and is less than 6 and not 0")
elif Last_digit > 5:
    print("Last digit of", number, "is", Last_digit, "and is greater than 5")
elif Last_digit < 6 and Last_digit!= 0:
    print("Last digit of", number, "is", Last_digit, "and is less than 6 and not 0")
else:
    print("Last digit of", number, "is", Last_digit, "and is 0")
