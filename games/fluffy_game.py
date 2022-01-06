from art import *
from more_functions import press_return_to_cont
from replit import clear

import random, time, string


def print_display():
    '''
    clears the screen and prints header, fluffy art ascii
    '''
    clear()
    print(fluffy_header)
    print()

    print(fluffy_art)
    print()


def print_flute_effectiveness(flute_effectiveness):
    '''
    get random integer 1-3, which increases flute effectiveness points by that number
    print results of flute effectiveness
    '''
    # At each turn, when the user plays the flute, they can lull Fluffy to sleep with random, equal chance of increasing flute_effectiveness by 1 - 3 points.
    playflute = random.randint(1,3)
    # if playflute is 3
    if playflute == 3:
        # increment flute_effectiveness by 3
        flute_effectiveness += 3
        # print what happens to fluffy when flute_effectiveness increases by 3
        print("*doo doo dee* Your playing sounds great!")
        print("Great, Fluffy is getting much sleepier!")
        print()
        # since there is a chance that flute_effectiveness may be greater than 10, if greater than 10
        if flute_effectiveness > 10:
            # set flute_effectiveness to 10
            flute_effectiveness = 10
    # else if playflute is 2
    elif playflute == 2:   
        # increment flute_effectiveness by 2
        flute_effectiveness += 2
        # print what happens to fluffy when flute_effectiveness increases by 2
        print("*dee da da* Your playing sounds ok.")
        print("Fluffy is getting slightly sleep!")
        print()
        # since there is a chance that flute_effectiveness may be greater than 10, if greater than 10
        if flute_effectiveness > 10:
            # set flute_effectiveness to 10
            flute_effectiveness = 10
    # else (playflute is 1)
    else:
        # increment flute_effectiveness by 1
        flute_effectiveness += 1
        # print what happens to fluffy when flute_effectiveness increases by 1
        print("*SQUAWK* Oops, you played a bit off tune.")
        print("Fluffy is barely getting sleepy!")
        print()
    # print total flute_effectiveness
    print(f"Flute's effectiveness: {flute_effectiveness}")

    # return new flute_effectiveness value
    return flute_effectiveness


def print_fluffy_waking(fluffy_waking, flute_effectiveness):
    '''
    if user has not won yet (flute effectiveness < 10), get random integer 1-3, which increases fluffy's likeliness to wake points by that number
    print results of fluffy's likeness to wake
    '''
    # If flute_effectiveness has not already reached 10 points, at each turn, Fluffy also has a chance to wake up.
        # There is a random, equal chance of increasing fluffy_waking by 1 - 3 points.
    if flute_effectiveness < 10:
        fluffywakens = random.randint(1,3)
        # if fluffywakens is 3
        if fluffywakens == 3:
            # increment fluffy_waking by 3
            fluffy_waking += 3
            # print what happens to fluffy when fluffy_waking increases by 3
            print()
            print("...uh oh!")
            print("*One of Fluffy's six eyes open*")
            print("Fluffy is starting to wake up!")
            print()
            # since there is a chance that fluffy_waking may be greater than 10 and fluffy_waking max is 10, set fluffy waking to 10
            if fluffy_waking > 10:
                fluffy_waking = 10
        # else if fluffywakens is 2
        elif fluffywakens == 2:
            # increment fluffy_waking by 2
            fluffy_waking += 2
            # print what happens to fluffy when fluffy_waking increases by 2
            print()
            print("...wait!")
            print("*Fluffy shakes his heads and all three heads yawn*")
            print("Is he waking up?")
            print()
            # since there is a chance that fluffy_waking may be greater than 10 and fluffy_waking max is 10, set fluffy waking to 10
            if fluffy_waking > 10:
                fluffy_waking = 10
        # else (fluffywakens is 1)
        else:
            # increment fluffy_waking by 1
            fluffy_waking += 1
            # print what happens to fluffy when fluffy_waking increases by 1
            print()
            print("*Fluffy's three heads snore loudly*")
            print("Oh good, he stayed asleep.")
            print()
            
        # print total fluffy_waking
        print(f"Fluffy's likeliness of waking: {fluffy_waking}")
        
    return fluffy_waking


# Define Fluffy game function
def fluffy_game():
    '''
    loops through the fluffy game until the user gets 10 points or fluffy gets 10 points. If user loses, restart the game.
    '''
    while True:
        # Set flute effectiveness points to 0
        flute_effectiveness = 0
        # Set fluffy likeliness to wake up points to 0
        fluffy_waking = 0
        # While user life is less than 10 and Fluffy's life is less than 10, play the game
        while fluffy_waking < 10 and flute_effectiveness < 10:
            # Print the header at the start of each loop
            print_display()
            
            # Ask user to press return as input for each turn to play the flute
            input("Press RETURN to play the flute")
            print()

            # call print_flute_effectiveness and set to flute_effectiveness
            flute_effectiveness = print_flute_effectiveness(flute_effectiveness)

            time.sleep(1)

            # call print_fluffy_waking and set to fluffy_waking
            fluffy_waking = print_fluffy_waking(fluffy_waking, flute_effectiveness)

            press_return_to_cont()

        # if flute_effectiveness is 10 (you win!)
        if flute_effectiveness == 10:
            print_display()
            # Print Fluffy has fallen asleep. Continue story
            # Have user press return to break the loop and continue the story
            print("YAY! Fluffy is finally fast asleep! Let's go through the trap door!")
            cont = press_return_to_cont()
            if cont is True:
                break
        # else (game ends when fluffy_waking is 10)
        else:
            print_display()
            # Print Fluffy wakes up
            # Have user press return to restart the game
            # Clear the screen
            # Call fluffy game function
            print("Oh no! Fluffy has woken up. Let's get out of here!")
            cont = False
            press_return_to_cont(cont)