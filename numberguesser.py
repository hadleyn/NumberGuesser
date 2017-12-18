# We need to tell Python that we want to use certain features so it can
# get them ready for us
# "sys" contains things that help us read user input and print things to the screen
# "math" contains things to help with advanced mathematical operations (beyond addition, subtraction, division, etc)
import math

# Our program/game has certain parameters or limits that need to be declared before we begin.
# You can change these values to change how the game ultimately works.
upperLimit = 100
lowerLimit = 1
guess = int(math.floor((upperLimit + lowerLimit) / 2))
totalGuesses = 1

# This is a calculation of how many tries it will take the guesser
magicGuesses = int(math.ceil(math.log((upperLimit - lowerLimit), 2)))

# The main game can now start!
print ("Magic Number Guesser!")
print ("I will always guess your number in " + str(magicGuesses) + " or fewer tries!\n\n")
print ("Think of a number between " + str(lowerLimit) + " and " + str(upperLimit))

response = input("Is your number greater than (1), less than (-1) or equal to (0) " + str(guess) + "?\n")



while response != 0:
    print ("Ok, let me try again!")
    totalGuesses = totalGuesses + 1
    if response == 1:
        lowerLimit = guess
        guess = int(math.floor((upperLimit + guess) / 2))
    elif response == -1:
        upperLimit = guess
        guess = int(math.floor((lowerLimit + guess) / 2))

    response = input("Is your number greater than (1), less than (-1) or equal to (0) " + str(guess) + "?\n")

print ("Hurrah! Your number was " + str(guess))
print ("It took me " + str(totalGuesses) + " tries")
