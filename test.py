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

def user(x):
    low=x
    high=1
    feedback=''
    while feedback !='c':
        guess= random.randint
        feedback=input(f"is the {guess}input too (H) or (L) or is it correct".lower)
        if feedback == 'h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
        
    print("yay congrats")

guess(10)