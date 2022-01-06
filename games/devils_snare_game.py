from art import *
from more_functions import press_return_to_cont
from replit import clear
from words import *

import random, time, string


# Create a list of Harry Potter words (words.py)

def get_hint(word, hint):
    '''
    if user inputs "hint" one time, print first hint
    if user inputs "hint" a second time, print second hint
    if user inputs "hint" a third time, print third hint
    if user inputs "hint" more than three times, print all hints
    '''
    if hint == 1:
        print(words[word]["Hints"][0])
    elif hint == 2:
        print(words[word]["Hints"][1])
    elif hint == 3:
        print(words[word]["Hints"][2])
    elif hint > 3:
        print(words[word]["Hints"][0])
        print(words[word]["Hints"][1])
        print(words[word]["Hints"][2])


def get_random_word():
    '''
    return a random word from the words dictionary
    '''
    word = random.choice(list(words))
    return word


def change_word_to_display(word):
    '''
    Change each letter of the word to "_", excluding spaces
    '''
    # Create a word_display empty list
    word_display = []
    # For each letter in word
        # Increment word_display by "_"
    for char in word:
        if char in string.ascii_lowercase:
            word_display += "_"
        else:
            word_display += char

    return word_display


def print_display(word_display, turns, already_guessed):
    '''
    clears the screen and prints header, word_display, number of turns remaining and letters guessed
    '''
    # print header
    clear()
    print(devils_snare_header)
    print()

    # print display
    print(" ".join(word_display))
    print()

    # Print number of turns left
    print(f"Turns remaining: {turns}")
    print()

    # Print guessed
    print("Letters guessed:", ", ".join(already_guessed))
    print()


def guess_function(word_display, turns, already_guessed):
    """
    Guess a letter or ask for hint; ensuring they pick a valid input.
    Return the guess.
    """
    # keep looping until user chooses a valid guess
    while True:
        print_display(word_display, turns, already_guessed)
        
        # Ask user to input one letter guess. Change input to lowercase.
        print("Guess a letter to beat the Devil's Snare or type \"hint\" for a hint (maximum three hints)")
        guess = input("> ")
        guess = guess.lower()
        print()

        # if input is one character and part of the alphabet, return guess
        if (len(guess) == 1) and (guess in string.ascii_lowercase):
            return guess
        elif guess == "hint":
            return guess
        
        # if the guess does not fulfill above requirements, loop again until the input is valid
        print("Invalid input. Please try again.")
        press_return_to_cont()


def update_word_display(word, guess, already_guessed, word_display, possible_guesses):
    '''
    update the word display with correct guesses; updates already guessed list and possible guesses list
    '''
    # for index and letter in the word (enumerate)
    for idx, letter in enumerate(word):
        # if guess is the letter (the guess is correct and in the word)
        if guess == letter:
            # set word_display at that index number to the correct answer
            word_display[idx] = guess
    # pop the guess from possible guesses and add to guessed list
    already_guessed += possible_guesses.pop(possible_guesses.index(guess))


def print_word_definition(word):
    '''
    parameter: word
    prints the title case of the word and definition from the words dictionary
    '''
    print(word.title())
    print(words[word]["Definition"])

        
# Define Devil's Snare game function
def devils_snare_game():
    '''
    loops through the devil's snare game until the user guesses the word or runs out of turns. If user loses, restart the game.
    '''
    while True:
        # Set word to random choice in words list
        word = get_random_word()

        # Change word into "_" for each letter
        word_display = change_word_to_display(word)

        # set hints to 0
        hint = 0

        # Set number of turns to 8
        turns = 8

        # Create a possible_guesses list for all characters of the alphabet
        possible_guesses = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        # Set already_guessed to empty list
        already_guessed = []

        # Loop while turns > 0
        while (turns > 0) and ("_" in word_display):

            # use guess function to assign guess variable (make sure user inputs valid guess)
            guess = guess_function(word_display, turns, already_guessed)

            if guess == "hint":
                hint += 1
                get_hint(word, hint)
                press_return_to_cont()
            # If guess is not in possible_guesses (list of letters that have not been guessed yet)
            elif guess not in possible_guesses:
                # Print you have guessed this letter already. Please try again.
                print("You have guessed this letter already. Please try again.")
                press_return_to_cont()
            # Else if guess is in word (and guess is a possible guess)
            elif guess in word:
                # Print Great guess!
                print("Great guess! 😄")
                press_return_to_cont()
                # update the word display with correct guess and add the guessed letter to already guessed list
                update_word_display(word, guess, already_guessed, word_display, possible_guesses)
            # Else if guess is not in word (and guess is a possible guess)
            elif guess not in word:
                # Print Wrong guess! 😔
                print("Wrong guess! 😔")
                press_return_to_cont()
                # decrement number of turns by 1
                turns -= 1
                # update the word display with correct guess and add the guessed letter to already guessed list
                update_word_display(word, guess, already_guessed, word_display, possible_guesses)
            
        # If "_" not in word_display (all the letters have been guessed)
        if "_" not in word_display:
            print_display(word_display, turns, already_guessed)
            # Print Congrats! You guessed the word and defeated the Devil's Snare
            print("Congrats! You guessed the word and defeated the Devil's Snare.")
            # break out of the loop when user guesses correct word
            print()
            print_word_definition(word)
            cont = press_return_to_cont()
            if cont is True:
                break
        # Else (did not win the game)
        else:
            print_display(word_display, turns, already_guessed)
            # Print Oh no! The Devil's Snare has swallowed you whole.
            # Have user press return to restart the game
            # Clear the screen
            print(f"Oh no! The word is {word.title()}. The Devil's Snare has swallowed you whole.")
            print()
            print_word_definition(word)
            cont = False
            press_return_to_cont(cont)