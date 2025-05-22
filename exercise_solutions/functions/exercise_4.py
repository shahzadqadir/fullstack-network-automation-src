# Problem
# Write a function that takes a number between 1 and 1000 from user, 
# generates a random number and check if the user supplied number is equal to randomly generated number, 
# if it is, tell user you have won. Otherwise tell user if his number was too low or too high. 
# The random number generated must be between 1 and 1000.

import random

def guessing_game(number: int) -> None:
    random_num = random.randint(1, 1001)
    # print(random_num)     # use this print statement to check what random number was generated
    if number == random_num:
        print("You have won")
    elif number > random_num:
        print("Number too high")
    else:
        print("Number too low")

guessing_game(566) 