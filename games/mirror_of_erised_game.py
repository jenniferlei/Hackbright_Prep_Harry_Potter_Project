from art import *
from more_functions import press_return_to_cont
from replit import clear

import random, time, string


def create_values_list():
    '''
    returns a value list for the 16 grids on the board
    '''
    values = []
    # for num of values (will have a 4 x 4 board = 16)
    for i in range(16):
        # increment values by a blank space ' '
        values += " "
    return values


# define print_board function with values as its parameter
def print_board(values_list):
    '''
    prints a 4x4 board as the "mirror" with values in each grid
    '''
    # print board with mirror of erised at the top
    # print 1 - 4 as header
    # print A - D on left side
    # print 4 x 4 squares with corresponding location value within each square
    print()
    print("\t      .:*¨¨¯¯¯¯¯¯¯¨¨*:.  ")
    print("\t    .*     erised      *.")
    print("\t  .* 1     2     3     4 *.")
    print("\t  _________________________")
    print("\t  |     |     |     |     |")
    print("\tA |  {}  |  {}  |  {}  |  {}  |".format(values_list[0], values_list[1], values_list[2], values_list[3]))
    print("\t  |_____|_____|_____|_____|")
    print("\t  |     |     |     |     |")
    print("\tB |  {}  |  {}  |  {}  |  {}  |".format(values_list[4], values_list[5], values_list[6], values_list[7]))
    print("\t  |_____|_____|_____|_____|")
    print("\t  |     |     |     |     |")
    print("\tC |  {}  |  {}  |  {}  |  {}  |".format(values_list[8], values_list[9], values_list[10], values_list[11]))
    print("\t  |_____|_____|_____|_____|")
    print("\t  |     |     |     |     |")
    print("\tD |  {}  |  {}  |  {}  |  {}  |".format(values_list[12], values_list[13], values_list[14], values_list[15]))
    print("\t  |_____|_____|_____|_____|")
    print()


def print_display(turns, values):
    '''
    clears the screen and prints header, board, and turns remaining
    '''
    clear()
    print(mirror_of_erised_header)
    print()

    # call print_board function
    print_board(values)

    # Print number of turns left
    print(f"Turns remaining: {turns}")
    print()


def guess_function(locations, turns, values):
    """Choose a location; ensuring they pick a valid location.

    Return the guess.
    """
    # keep looping until user chooses a valid location
    while True:
        print_display(turns, values)
        # ask user for guess input. Change to uppercase.
        print("Guess the location of the sorcerer's stone. Example: A1")
        guess = input("> ")
        guess = guess.upper()
        print()

        # if guess is valid return guess
        if guess in locations:
            return guess

        # otherwise, print error message and have user try again
        print_display(turns, values)
        print("That isn't a location on the mirror. Please try again.")
        press_return_to_cont()


# Define mirror_of_erised game function
def mirror_of_erised_game():
    '''
    loops through the mirror of erised game until the user finds the stone position or runs out of turns. If user loses, restart the game.
    '''
    while True:
        # Create an empty list (values) for all the possible locations the rock could be
        values = create_values_list()

        # Create locations list ["A1", "A2", "A3", etc]
        locations = ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4", "D1", "D2", "D3", "D4"]

        # Create empty guessed_locations list
        guessed_locations = []

        # Set sorcerer's stone_position to a random choice of the locations list
        stone_position = random.choice(locations)

        # Set turns to 12
        turns = 12

        guess = ''

        # While turns > 0
        while turns > 0 and guess != stone_position:
            print_display(turns, values)

            guess = guess_function(locations, turns, values)
            
            # Else if guess is not in guessed_locations
            if guess not in guessed_locations:
                # Change the values list at locations guess index to 'X'
                values[locations.index(guess)] = 'X'
                # Add guess to guessed_locations
                guessed_locations.append(guess)

                # Decrement turns by 1
                turns -= 1
            # Else
            elif guess in guessed_locations:
                # Print You have already guessed this location. Please try again.
                print("You have already guessed this location. Please try again.")
                press_return_to_cont()
        # If guess is equal to the stone_position (You found the stone!)
        if guess == stone_position:
            # Change the values list at locations guess index to 'O' to mark where the stone is
            values[locations.index(guess)] = 'O'
            # print display
            print_display(turns, values)
            # Print You found the sorcerer's stone! 🪨 Keep it safe!
            print("You found the sorcerer's stone! 🪨  Keep it safe from Professor Quirrel!")
            cont = press_return_to_cont()
            if cont is True:
                break
        # Else (did not get correct potion_number)
        else:
            # Print Oh no! Professor Quirrell found the stone before you.
            # Have user press return to restart the game
            # Clear the screen before starting the loop over
            print("Oh no! Professor Quirrel found the sorcerer's stone before you. ")
            cont = False
            press_return_to_cont(cont)