import random, time
from art import *
from wand_features import *
from more_functions import press_return_to_cont
from replit import clear


def random_wood():
    '''
    Chooses a random core from the wand_woods dictionary
    '''
    wood = random.choice(list(wand_woods))
    return wood


def random_core():
    '''
    Chooses a random core from the wand_cores dictionary
    '''
    core = random.choice(list(wand_cores))
    return core


def random_length():
    '''
    Chooses a random length between 9 and 14 inches
    '''
    length = random.randint(9, 14)
    length2 = random.choice(wand_lengths)
    total_length = f"{length} {length2}"
    return total_length


def random_flexibility():
    '''
    Chooses a random flexibility
    '''
    flexibility = random.choice(wand_flexibility)
    return flexibility
    

def wand_info(wood, core):
    '''
    Prints wand info from the wand_woods and wand_cores dictionaries
    '''
    print(wood)
    print("Wand wood information:")
    print(wand_woods[wood])
    print()
    print(core)
    print("Wand core information:")
    print(wand_cores[core])
    print()
    print("Text from www.wizardingworld.com")
    

def wand_game():
    '''
    Selects the wood, core, length and flexibility of the wand and prints your wand details
    '''
    print(ollivanders_header)
    print()

    wood = random_wood()
    core = random_core()
    total_length = random_length()
    flexibility = random_flexibility()

    print(f"""Ollivander studies the wand that has chosen you.

Ah yes, your wand is made of {core} core and {wood} wood.
{total_length} and {flexibility} flexibility. Very interesting.
""")

    time.sleep(1)

    print(ollivander_wand)

    # Give the user the option to read more info about their wand
    info = input("""If you would like more information about your wand, enter \"I\".
Otherwise, press RETURN to continue """)
    info = info.lower()

    if info.startswith("i"):
        clear()
        wand_info(wood, core)
        press_return_to_cont()
    else:
        clear()