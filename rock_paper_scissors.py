import random

def play():
    user=input("(R) for rock, (P) for paper, (S) for scissors \n").lower()
    computer=random.choice(['r','p','s'])
    user_won=0
    com_won=0
    while user_won!=10:
        if user==computer:
            return "its a tie"
        elif is_win(user,computer):
            user_won+=1
            return f"You won {user_won} rounds"
        com_won+=1
        return f"You lost ! {com_won} rounds"

def is_win(player,opponent):
    if player=='r' and opponent=='s' or player=='s' and opponent=='p' or player=='p'and opponent=='r':
        return True
print(play())