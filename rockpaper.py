import random
def play():
    user=input("r for rocks,p for paper,s for scissors" )
    comp=random.choice(['r','p','s'])

    if user==comp:
        return 'tie'
    if is_win(user,comp):
        return 'you won'
    return 'you lost'

    #r>s,s>p,p>r
def is_win(user,comp):
    return(user=='r' and comp=='s') or (user=='s' and comp=='p') or (user=='p' and comp=='r')
    

print(play())