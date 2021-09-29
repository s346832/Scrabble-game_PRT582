import unittest
from random import randint
import enchant
from time import *
import threading


class MyTest(unittest.TestCase):
    # requirement:FR-001. Testing to check value of letter.
    def test_letter_value(self):
        self.assertEqual(score["a"], 1)
        self.assertEqual(score["b"], 3)
        self.assertEqual(score["z"], 10)

    # requirement:FR-002,FR-003. Testing to check value of words mixed with upper-or-lower case letter.
    def test_word_value(self):
        assert 14 == scrabble_score("cabbage")
        assert 7 == scrabble_score("sport")
        assert 14 == scrabble_score("Cabbage")
        assert 14 == scrabble_score("CABBAGE")
        assert 7 == scrabble_score("sPoRt")

    # requirement:FR-004. Testing to check the length of required input word is 3-10, which is generated randomly.
    def test_generate_random_length(self):
        self.assertIn(char_length, list_length)

    # requirement: FR-005. Testing to check word length
    def test_word_length(self):
        self.assertTrue(check_word_length("university", 10))
        self.assertTrue(check_word_length("study", 5))

    # requirement:FR-006. Testing to check alphabet
    def test_word_alphabet(self):
        self.assertTrue(check_alphabet("university"))
        self.assertTrue(check_alphabet("sport"))

    # requirement:FR-007. Testing to check the input word is valid from dictionary
    def test_dictionary(self):
        self.assertTrue(check_dictionary("university"))
        self.assertTrue(check_dictionary("cabbage"))

    # requirement:FR-008. Testing timer by using threading.
    def test_timer(self):
        countdown_thread = threading.Thread(target=countdown)
        countdown_thread.start()
        self.assertTrue(countdown)

    # requirement:FR-009. Testing higher score if less time is used to enter the word as required.
    def test_time_score(self):
        self.assertGreater((total_score("cabbage", 5)), (total_score("cabbage", 3)))


####
# Coding before refactoring
####
# assign values to letters.
score = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4,
         "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
         "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
         "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
         "y": 4, "z": 10}


# function to return the scrabble score for a given word
def scrabble_score(word):
    points = 0
    for letter in word.lower():
        points += score[letter]
    return points


# the length of required input word is 3-10, which is generated randomly.
char_length = randint(3, 10)
list_length = [3, 4, 5, 6, 7, 8, 9, 10]


# function to check word length, return true if word length is equal with required length
def check_word_length(word, require_len):
    word_length = len(word)
    if word_length == require_len:
        return True
    else:
        return False


# function to check input if it is alphabet
def check_alphabet(word):
    if word.isalpha():
        return True
    else:
        return False


# function to check input if it is valid word from dictionary
def check_dictionary(word):
    dictionary = enchant.Dict("en_US")
    if dictionary.check(word):
        return True
    else:
        return False


# function to make 15 sec timer
def countdown():
    global my_timer
    my_timer = 15
    for x in range(15):
        if my_timer == 0:
            return True
            break
        my_timer = my_timer - 1
        sleep(1)


# function to give higher score if less time is used.
def total_score(word, my_timer):
    overall_score = 0
    dictionary = enchant.Dict("en_US")
    if word.isalpha() and my_timer > 0:
        if dictionary.check(word):
            overall_score = overall_score + scrabble_score(word)*my_timer
            return overall_score


if __name__ == '__main__':
    unittest.main()


