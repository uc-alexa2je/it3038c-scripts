print("This is a number guessing game")

from operator import truediv
import time

#generate a random integer
from random import seed
from random import randint
from typing import NoReturn, no_type_check, no_type_check_decorator

#seed random number generator
seed(1)

#generate integer
for _ in range(1):
  value = randint(0, 100)

#Start game

print("What is your name?")
myName = input()
print("Hello " + myName + ".  Please select a number between 0 - 100.")
myGuess = input()
print("Your guess is " + myGuess)

#Pause after showing guessed number
time.sleep(4)

#begin eval
if int(myGuess) < value:
    print("You are too low!")

elif int(myGuess) == value:
    print("You are correct! The number is: " + value)

elif int(myGuess) > value and int(myGuess) <= 100:
    print("You are too high!  Try again.")

elif int(myGuess) > 100:
    print("You are out of range.  Please select between 0 - 100.")

#End the game
while True:
    print("Would you like to play again?")
    reply = input()
    

        
    if reply == no_type_check or reply == no_type_check:
        print("The random number was: " + str(value))
        break
        print("Have a nice day!")

    
