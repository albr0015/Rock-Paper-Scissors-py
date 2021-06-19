import random

def game(): 

    player = input("choose option:\n 'r'- Rock, 'p' - Paper, 's'- Scissors\n")
    computer = random.choice(['r','p','s'])

    if player == computer: 
        return 'draw up'

    if winner(player, computer):
        return 'You Win!'
    
    return 'You Lose!'

def winner(player, computer):
    if(player == 'r' and computer == 's') or (player == 's' and computer == 'p') \
        or (player == 'p' and computer == 'r'): 
        return True 


print(game())


