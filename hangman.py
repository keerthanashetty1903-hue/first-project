import random
from words import words
import string

def get_valid_word(words):
    word= random.choice(words)
    while '-' in word or ' ' in word:
        word= random.choice(words)

    return word

def hangman():
    word=get_valid_word(words)
    word_letters=set(word.upper())
    alpha=set(string.ascii_uppercase)
    used=set()

    user_letter=input('guess the input').upper()
    if user_letter in alpha -used:
        used.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)



    elif user_letter in used:
        print('youve already guessed it')

    else:
        print('enter a valid character')

user_input=input('enter the input')
print(user_input)
hangman()