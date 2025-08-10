import random

def guess(x):
    rand_num=random.randint(1,x)
    guess=0
    while guess != rand_num:
        guess =int(input('enetr the guess number'))

        if guess < rand_num :
            print('the number is too low ')
        elif guess > rand_num:
            print('the num is too high try again')

    print('yay you guessed it right')

guess(10)