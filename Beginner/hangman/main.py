import random
import string
from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    word - get_valid_word(words)
    word_letters = set(word)    # Letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # Keep track of guessed letters

    # Getting user input
    user_letter = input('Guess a number:\n').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add()
        if user_letter in word_letters:
            word_letters.remove(used_letters)

    elif user_letter in used_letters:
        print('You have already guessed that! Try again.')

    else:
        print('Invalid character, please try again!')


hangman()