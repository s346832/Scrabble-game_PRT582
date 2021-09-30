import sys
from random import randint
import enchant
from time import *
import threading

# give points/scores for letters。
score = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4,
         "g": 2, "h": 4, "i": 1, "j": 8, "k": 5,  "l": 1,
         "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
         "s": 1, "t": 1, "u": 1, "v": 4, "w": 4,  "x": 8,
         "y": 4, "z": 10}


# define a function to return the scrabble score for a given word.
# upper and lower case will have same values because whatever the user input,
# it will change to lowercase by using the word.lower() function.
def scrabble_score(word):
    points = 0
    for letter in word.lower():
        points += score[letter]
    return points


# make a 16 sec timer. There will be 15 sec to play the game after press "run".
def countdown():
    global my_timer
    my_timer = 16
    for x in range(16):
        if my_timer == 0:
            break
        my_timer = my_timer - 1
        sleep(1)
    print( "\nTIME IS UP!\n", "YOUR TOTAL SCORE IS :", total_score)


# using threading for timer. It will delay 16 sec until finish game according to the set above.
countdown_thread = threading.Thread(target=countdown)
countdown_thread.start()
# using dictionary for later to check whether user enters a valid word from a dictionary.
dictionary = enchant.Dict("en_US")

total_score = 0
while my_timer > 0:
    char_length = randint(3, 10)  # the length of required input word is 3-10, which is generated randomly.
    print("You only have", my_timer, "seconds to play!")
    print("Please enter a Word (", char_length, "alphabet) : ")
    userInput = input().lower().replace(" ", "")

    if userInput.isalpha() and len(userInput) == char_length and my_timer > 0:
        # if the input is alphabet, in right length and in the dictionary, count the total score.
        if dictionary.check(userInput):
            total_score = total_score + scrabble_score(userInput)*my_timer
            print("Your Score is :", total_score, "and you finished in", 15-my_timer, "seconds")
        else:
            print("Your input is not an English Word!")

    if userInput.isalpha() is False and my_timer > 0:
        print("Your input is not alphabet!")

    if len(userInput) != char_length and userInput.isalpha() and my_timer > 0:
        print("Length of your Word is not same with the requirement!")

