# Harry Potter Game

# import all games - is there a way to shorten this?
from games.wand_game import *
from games.pet_game import *
from games.sorting_hat_game import *
from games.fluffy_game import *
from games.devils_snare_game import *
from games.guess_potion_game import *
from games.mirror_of_erised_game import *
from games.voldemort_encounter_game import *
from more_functions import press_return_to_cont
from art import *
from story import *
from words import *

import random, time, string
from replit import clear

# Print game header
print(harrypotterlogo)

# Call function to clear before moving onto next story
press_return_to_cont()

# Print the entrance letter welcoming the user to start school at Hogwarts
print(hogwarts_letter)

# Call function to clear before moving onto next story
press_return_to_cont()

# Call function to print Diagon Alley story
diagon_alley_story()

# Call function to clear before moving onto next story
press_return_to_cont()

# Call function to print Ollivander's Wand Shop story
ollivanders_story()

# Call function to clear before moving onto next story
press_return_to_cont()

# play wand_game
    # NICE TO HAVE : QUIZ
wand_game()

# Call function to print Magical Menagerie story
menagerie_story()

# Call function to clear before moving onto next story
press_return_to_cont()

# set pet variable to pet_game function
    # NICE TO HAVE : QUIZ
pet = pet_game()

# Call function to clear before moving onto next story
press_return_to_cont()

# Call function that prints the welcome story, about starting school at Hogwarts
welcome_story(pet)

# Call function to clear before moving onto next story
press_return_to_cont()

# print castle ascii
print(hogwarts_castle)

# Call function to clear before moving onto next story
press_return_to_cont()

# Call function that prints the welcome story part 2
welcome_story2()

# Call function to clear before moving onto next story
press_return_to_cont()

# Call function that prints the sorting hat story
sorting_hat_story()

# Call function to clear before moving onto next story
press_return_to_cont()

# Set house variable to sorting hat game function to sort the user into one of the four Hogwarts houses with a short quiz
house = sorting_hat_game()

# Call function that prints the year 1 story
year1_story()

# Call function to clear before moving onto next story
press_return_to_cont()

########## Obstacle 1: Fluffy, the three headed dog ##########

# Call function to print story and rules for Fluffy game: 
fluffy_story()

# Call function to clear before moving onto next story
press_return_to_cont()

# Call Fluffy game (play the flute to put Fluffy, the three headed dog, to sleep. Similar to Darth COBOL from the Mars Adventure exercise)
fluffy_game()


########## Obstacle 2: Devil's Snare, the constricting plant (Harry Potter Hangman) ##########

# Call function to print story and rules for devils_snare game: 
devils_snare_story()

# Call function to clear before moving onto next story
press_return_to_cont()

# Call devils_snare game (Hangman)
devils_snare_game()

########## NICE TO HAVE: Obstacle 3: Flying Keys ##########

########## NICE TO HAVE: Obstacle 4: Wizards Chess ##########

########## Obstacle 5: Guess the Potion (Guess the number) ##########

# Call function to print story and rules for guess_the_potion game: 
guess_potion_story()

# Call function to clear before moving onto next story
press_return_to_cont()

# Call guess_the_potion game function (guess the correct number from 1 - 10)
guess_potion_game()

########## Obstacle 6: Mirror of Erised (Harry Potter battleship) ##########

# Call function to print story and rules for encounter_with_voldemort game: 
mirror_of_erised_story()

# Call function to clear before moving onto next story
press_return_to_cont()

# Call mirror_of_erised game function
mirror_of_erised_game()

########## Obstacle 7: Encounter with Voldemort (Harry Potter rock paper scissors) ##########

# Call function to print story and rules for voldemort_encounter game: 
voldemort_encounter_story()

# Call function to clear before moving onto next story
press_return_to_cont()

# Call voldemort_encounter game
voldemort_encounter_game()

# Call function to print end story.
year1_end_story(house)

# Call function to clear before moving onto next story
press_return_to_cont()

# Call function to print end credits
credits()