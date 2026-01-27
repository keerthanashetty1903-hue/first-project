import random
def user(x):
    low=1
    high=x
    feedback=''
    while feedback !='c':
        if low !=high:
            guess = random.randint(low,high)
        else:
            guess=low
        feedback=input(f"is the {guess}input too (H) or (L) or is it (C)").lower()
        if feedback == 'h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
        
    print("yay congrats")

user(10)