import random

def number():
    number = random.randint(1,100)
    guess = 0

    while guess != number:
        guess = int(input("enter guess number: "))
        
        if (guess<number):
            print("guess high!...")
        elif(guess>number):
            print("guess low!....")
        else:
            print("you won! ")
