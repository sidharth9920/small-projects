import random

def number_guesser(x):
    num=random.randint(1,x)
    guess=0
    while num!=guess:
        guess=int(input(f"Guess a number bitween 1 and {x} :"))
        if num>guess:
            print("To Low")
            
        elif num<guess:
            print("To High")
            
    print(f"Correct Guess {num}")

number_guesser(10)

def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        guess=random.randint(low,high)
        print(f"Is your number {guess}")
        feedback=str(input("c-Correct, L-to go lower, h-to go higher")).lower()
        if feedback=="l":
            high-=1
        elif feedback=="h":
            low+=1
    print(f"Got it the number is {guess}")

computer_guess(10)