import random
from art import *
from replit import clear
from more_functions import press_return_to_cont


house_dict = {
    "Gryffindor": [gryffindor_header, """Gryffindor valued bravery, daring, nerve, and chivalry.
Its emblematic animal was the lion, and its colours were scarlet and gold.
Minerva McGonagall was the most recent Head of Gryffindor.
Sir Nicholas de Mimsy-Porpington, also known as "Nearly Headless Nick", was the House Ghost.
The founder of the House was Godric Gryffindor. Gryffindor corresponded to the element of Fire.
The common room was located in one of the highest towers at Hogwarts, the entrance was situated
on the seventh floor in the east wing of the castle and was guarded by a portrait of The Fat Lady.
She permitted entrance if given the correct password, which was changed numerous times throughout
the school year.
Famous Gryffindors included Albus Dumbledore, Harry Potter, and Minerva McGonagall."""],
    "Slytherin": [slytherin_header, """Slytherin valued ambition, leadership, self-preservation, cunning and resourcefulness
and was founded by Salazar Slytherin.
Its emblematic animal was the serpent, and its colours were emerald green and silver.
Professor Horace Slughorn was the Head of Slytherin during the 1997–1998 school year,
replacing Severus Snape, who as well replaced Slughorn as Potions Professor when he
retired for the first time several years prior.
Slytherin had produced the most Death Eaters and Dark Wizards, including Tom Riddle,
Bellatrix Lestrange and Lucius Malfoy, for example.
But that does not mean that other Houses hadn't produced any;
Peter Pettigrew was a Gryffindor, and Quirinus Quirrell was a Ravenclaw.

The Bloody Baron was the House ghost.
The founder of the House was Salazar Slytherin. Slytherin corresponded roughly to the element of water.
The Slytherin dormitories and common room were reached through a bare stone wall in the Dungeons.
The Slytherin common room lay beneath the Black Lake.
It was a long, low underground room with rough stone walls and silver lamps hanging from the ceiling.
Famous Slytherins included Merlin, Tom Riddle, Draco Malfoy, and Dolores Umbridge."""],
    "Ravenclaw": [ravenclaw_header, """Ravenclaw valued intelligence, knowledge, curiosity, creativity and wit.
Its emblematic animal was the eagle, and its colours were blue and bronze.
The Ravenclaw Head of House in the 1990s was Filius Flitwick.
The ghost of Ravenclaw was the Grey Lady, who was the daughter of Rowena Ravenclaw, the House's founder.
Ravenclaw corresponded to the element of air.
The Ravenclaw common room and dormitories were located in a tower on the west side of the castle.
Ravenclaw students must answer a riddle as opposed to giving a password to enter their dormitories.
This riddle, however, could be answered by non-Ravenclaws.
Famous Ravenclaws included Luna Lovegood, Gilderoy Lockhart,
Ignatia Wildsmith (inventor of Floo powder), and Garrick Ollivander."""],
    "Hufflepuff": [hufflepuff_header, """Hufflepuff valued hard work, dedication, patience, loyalty, and fair play.
Its emblematic animal was the badger, and yellow and black were its colours.
Pomona Sprout was the Head of Hufflepuff during 1991–1998, Sprout left the post of Head of Hufflepuff
and Herbology Professor sometime before 2017 and her successor for the position of Head of Hufflepuff
was currently unknown.
The Fat Friar was its ghost. The founder of the House was Helga Hufflepuff.

Hufflepuff corresponded to the element of earth.
The Hufflepuff dormitories and common room were located somewhere in the basement, near the castle's kitchens.
It could be accessed by tapping the barrel two from the bottom, middle of the second row in the rhythm of
"Helga Hufflepuff" and was described as being a cosy and welcoming place with yellow hangings, fat armchairs,
and underground tunnels that led to the dormitories, which had perfectly round doors, similar to barrel tops.
Famous Hufflepuffs included Hengist of Woodcroft (founder of Hogsmeade), Newt Scamander
(author of Fantastic Beasts and Where to Find Them), and Artemisia Lufkin (first female minister for magic)."""]}


def answer_function():
    """
    Input a letter a or b; ensuring they pick a valid input.
    Return the input.
    """
    while True:
        # Ask user to input for input
        answer = input("\t> ").lower()
        print()

        # if answer is a or b, return answer
        if answer == "a" or answer == "b":
            return answer

        # if the guess does not fulfill above requirements, loop again until the input is valid
        print("Invalid input. Please try again.")


def sorting_hat_quiz():
    '''
    Ask user for answers to quiz
    '''
    print("""\tWhen you’re making a decision, you…
        A. Weigh your options and go with your gut
        B. Analyze and choose the option with best possible outcome""")
    q1 = answer_function()

    print("""\tA bully is picking on your friend. Eventually they both go different ways. You first follow…
        A. Your friend
        B. The bully""")
    q2 = answer_function()

    return (q1, q2)


def house_results(answers):
    '''
    return results of quiz
    '''
    if answers == ("a", "a"):
        house = "Hufflepuff"
    elif answers == ("b", "b"):
        house = "Slytherin"
    elif answers == ("a", "b"):
        house = "Gryffindor"
    elif answers == ("b", "a"):
        house = "Ravenclaw"
    
    return house


def house_info(house):
    '''
    Prints house info
    '''
    # Depending on house, print header and defintion
    if house == "Gryffindor":
        print(house_dict["Gryffindor"][0])
        print()
        print(house_dict["Gryffindor"][1])
    elif house == "Slytherin":
        print(house_dict["Slytherin"][0])
        print()
        print(house_dict["Slytherin"][1])
    elif house == "Ravenclaw":
        print(house_dict["Ravenclaw"][0])
        print()
        print(house_dict["Ravenclaw"][1])
    elif house == "Hufflepuff":
        print(house_dict["Hufflepuff"][0])
        print()
        print(house_dict["Hufflepuff"][1])
    print()
    print("Text from https://harrypotter.fandom.com/wiki/Hogwarts_Houses")


def sorting_hat_game():
    '''
    randomly select one of the four Hogwarts houses and prints which house the user is in
    '''
    print(sorting_hat_header)
    print()
    print("""When your name is called, you walk up to the Sorting Hat.
The walk up feels like an eternity.
Your heart races. Which house will you be sorted in?

You place the Sorting Hat on your head, and you hear the hat say

    \"Ahh, hmm, interesting. Answer this...
""")

    # set answers from sorting hat quiz function
    answers = sorting_hat_quiz()

    # set house to house results function
    house = house_results(answers)

    # print results
    print(f"""\tI think you would fit best in...

    {house.upper()}!\"
""")

    info = input("""If you would like more information about your house, enter \"I\".
Otherwise, press RETURN to continue """)
    info = info.lower()

    # get more info on house or continue
    if info.startswith("i"):
        clear()
        house_info(house)
        press_return_to_cont()
    else:
        clear()

    return house