from art import *
from more_functions import press_return_to_cont
from replit import clear

import random, time, string


def print_display(turns):
    '''
    clears the screen and prints header, potions ascii
    '''
    clear()
    print(guess_potion_header)
    print()

    print(potions)
    print()

    print(f"Turns remaining: {turns}")
    print()


def guess_function(turns):
    """Guess an integer greater or equal to 1 and less than or equal to 10; ensuring they pick a valid integer.

    Return the guess.
    """
    # keep looping until user chooses a valid location
    while True:
        print_display(turns)

        # ask user for guess input
        guess = input("Guess a potion number 1 to 10: ")
        print()

        # if guess is numeric, change to integer
        if guess.isnumeric():
            guess = int(guess)
            # if guess is less than 1 or greater than 10, print error message and have user try again
            if (guess >= 1) and (guess <= 10):
                return guess
        # otherwise, print error message and have user try again 
        print("This potion does not exist. Please try again.")
        press_return_to_cont()


def check_guess(guess, potion_number):
    '''
    Check if the guess is less than or greater than the correct number
    '''
    # if guess is greater than potion_number
    if guess > potion_number:
        # Print Sorry, that is not the correct potion. Try a lower number!
        print("Sorry, that is not the correct potion. Try a lower number!")
        press_return_to_cont()
        
    # Else if guess is less than potion number
    elif guess < potion_number:
        # Print Sorry, that is not the correct potion. Try a higher number!
        print("Sorry, that is not the correct potion. Try a higher number!")
        press_return_to_cont()


# Define guess_the_potion game function
def guess_potion_game():
    '''
    loops through the guess potion game until the user guesses the correct potion number or runs out of turns. If user loses, restart the game.
    '''
    while True:
        # Set potion_number to random integer between (and including) 1 and 10
        potion_number = random.randint(1, 10)

        # Set number of guesses to 4 and guess number to 0
        turns = 4

        guess = 0

        # While number of turns is greater than 0 and correct potion number is not guessed yet,
        while (turns > 0) and (guess != potion_number):
            # Ask user for integer input for their guess from 1 to 10
            guess = guess_function(turns)
            turns -= 1
            check_guess(guess, potion_number)
                
        # If guess is the correct potion_number
        if guess == potion_number:
            print_display(turns)
            # Print You guessed the right one!
            print("You guessed the correct potion! This will get us safely through the black fire. ")
            # Ask for RETURN input to continue
            cont = press_return_to_cont()
            if cont is True:
                break
        # Else (did not get correct potion_number)
        else:
            print_display(turns)
            # Print Oh no! You picked the wrong potion.
            # Have user press return to restart the game
            # Clear the screen
            # Call guess_the_potion game function
            
            print("Oh no! You chose poison")
            print(poison_potion)
            cont = False
            press_return_to_cont(cont)