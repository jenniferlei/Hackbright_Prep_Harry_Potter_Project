import random
from art import *
from more_functions import press_return_to_cont

pets_list = ["Barn Owl", "Brown Owl", "Eagle Owl", "Golden Owl", "Great Grey Owl", "Little Owl", "Scops Owl", "Screech Owl", "Snowy Owl", "Tawny Owl", "Giant Purple Toad", "Horned Toad", "Common Toad", "Crested Toad", "Harlequin Toad", "Western Green Toad", "Natterjack Toad", "Black Cat", "Ginger Cat", "Siamese Cat", "White Cat", "Tabby Cat", "Half-cat half-kneazle"]


def name_the_pet(pet_type):
    '''
    ask for user to input pet name; ensure they pick a valid name.
    '''
    while True:
        # ask user for name and change to title case
        pet_name = input(f"What would you like to name your new {pet_type}? ").title()
        pet_name = pet_name.title()

        # if name is valid, return name
        if len(pet_name) > 0:
            return pet_name

        # otherwise, print error message and have user try again 
        print("Invalid input. Please try again.")
        print()


def pet_game():
    '''
    name and select a random animal from the menagerie
    '''
    print(menagerie_header)
    print()
    print("This one will do!")
    # random select from possible pets list
    pet_type = random.choice(pets_list)

    print(f"You point to a {pet_type}.")
    print()
    pet_name = name_the_pet(pet_type)
    pet = f"{pet_name} the {pet_type}"

    print()
    print(f"You have an instant connection with {pet}!")

    if "Cat" in pet_type:
        print(f"{pet} meows and jumps up to the top of your head.")
    elif "Toad" in pet_type:
        print(f"""{pet} hops onto the side of your face and
catches a fly that had been buzzing nearby.""")
    elif "Owl" in pet_type:
        print(f"{pet} flies over to your shoulder, hoots, and falls asleep.")
    print(f"You pay the shopkeeper and scurry out with {pet}.")
    print()
    print("Mission accomplished! Your day at Diagon Alley is done!")

    return pet
