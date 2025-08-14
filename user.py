import random
def user(x):
    low=1
    high=x
    feedback=''
    while feedback !='c':
        guess = random.randint(low,high)
        feedback=input(f"is the {guess}input too (H) or (L) or is it (C)").lower()
        if feedback == 'h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
        
    print("yay congrats")

user(10)