from art import *
from more_functions import press_return_to_cont
from replit import clear

import random, time, string


def print_display(round):
    '''
    clears the screen and prints header, wands ascii, round #
    '''
    clear()
    print(voldemort_encounter_header)
    print()

    print(wands)
    print()

    if round > 3:
        round = 3
    # Print number of turns left
    print(f"Round #: {round}")
    print()
    

def spell_function(round):
    """
    Cast a spell; ensuring they pick a valid spell integer.
    Return the spell.
    """
    while True:
        print_display(round)
        # Ask user for integer input of their spell out of three choices ([1] rock = Stupefy, [2] paper = Expelliarmus, [3] scissors = Confundo)
        spell = input("Cast a spell! [1] Rock/Stupefy, [2] Paper/Expelliarmus, [3] Scissors/Confundo: ")

        # if the spell is numeric, change to an integer
        if spell.isnumeric():
            spell = int(spell)
            # if spell is from 1 - 3, return the spell
            if (spell >= 1) and (spell <= 3):
                return spell
            else:
                print()
                print("The spell did not work. Please try again.")
                press_return_to_cont()
        
        print()
        print("The spell did not work. Please try again.")
        press_return_to_cont()

    

def spell_name(spell_num):
    '''
    param spell_num: user input 1, 2, or 3
    Return spell (string)
    '''
    if spell_num == 1:
        spell = "Stupefy"
    elif spell_num == 2:
        spell = "Expelliarmus"
    else:
        spell = "Confundo"
    return spell
    

# Define voldemort_encounter game function
def voldemort_encounter_game():
    '''
    loops through the voldemort encounter game for three rounds. If user loses or ties, restart the game.
    '''
    while True:
        # Set beginning game round and points
        # Set round to 1
        round = 1
        # Set user_points to 0
        user_points = 0
        # Set voldemort_points to 0
        voldemort_points = 0

        # While round is less than or equal to 3
        while round <= 3:
            print_display(round)
            
            # Have user select the spell with spell_function
            user_spell_num = spell_function(round)
            
            # Randomly select voldemort_spell from the three choices
            voldemort_spell_num = random.randint(1,3)

            # Print user_spell and voldemort_spell
            user_spell_name = spell_name(user_spell_num)
            voldemort_spell_name = spell_name(voldemort_spell_num)
            print(f"You cast {user_spell_name}! Lord Voldemort cast {voldemort_spell_name}!")
            print()

            # if user and voldemort spells are the same
                # Print Draw. Try again.
            if user_spell_num == voldemort_spell_num:
                print("The spells deflected off each other! Cast another spell.")
                print()

            # else if user_spell is 1 (rock/Stupefy) and voldemort_spell is 3 (scissors/Confundo)
                # Print user won and increment user_points by 1
            elif (user_spell_num == 1) and (voldemort_spell_num == 3):
                print("You beat Lord Voldemort this round!")
                print()
                user_points += 1

            # else if user_spell is 3 (scissors/Confundo) and voldemort_spell is 1 (rock/Stupefy)
                # Print user lost and increment voldemort_points by 1
            elif (user_spell_num == 3) and (voldemort_spell_num == 1): 
                print("Lord Voldemort beat you this round!")
                print()
                voldemort_points += 1

            # else if user_spell is greater than voldemort_spell (scissors/Confundo > paper/Expelliarmus, paper/Expelliarmus > rock/Stupefy)
                # Print user won and increment user_points by 1
            elif user_spell_num > voldemort_spell_num:
                print("You beat Lord Voldemort this round!")
                print()
                user_points += 1

            # else if voldemort_spell is greater than user_spell (scissors/Confundo > paper/Expelliarmus, paper/Expelliarmus > rock/Stupefy)
                # Print user lost and increment voldemort_points by 1
            elif voldemort_spell_num > user_spell_num:
                print("Lord Voldemort beat you this round!")
                print()
                voldemort_points += 1

            # print number of points and increment round by 1 at each turn
            print(f"Your wins: {user_points}\tLord Voldemort wins: {voldemort_points}")
            press_return_to_cont()

            round += 1

        # if user_points is greater than voldemort_points, print user defeated voldemort and continue the story
        if user_points > voldemort_points:
            print_display(round)
            print("Hooray! You have defeated Lord Voldemort! 😊")
            cont = press_return_to_cont()
            if cont == True:
                break
        # else if user points is equal to voldemort_points. print it's a draw and have user restart the game
        elif user_points == voldemort_points:
            print_display(round)
            print("It's a draw! Please try again. 😐")
            cont = False
            press_return_to_cont(cont)
        # else, print voldemort has defeated the user and have user restart the game
        else:
            print_display(round)
            print("Oh no! Lord Voldemort defeated you. 😫")
            cont = False
            press_return_to_cont(cont)