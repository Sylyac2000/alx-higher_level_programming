#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    reste = number % 10
else:
    reste = number % (-10)

if reste > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, reste))
elif reste == 0:
    print("Last digit of {} is {} and is 0".format(number, reste))
else:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, reste))
