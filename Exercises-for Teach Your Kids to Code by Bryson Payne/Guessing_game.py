# Guessing game
import random
the_number=random.randint(1,10)
guess=int(input("Guess a number between 1-10: "))
while guess!=the_number:
    if guess>the_number:
        print(guess, "was too high, try again")
    if guess<the_number:
        print(guess,"was too low, try again")
    guess=int(input("Guess again: "))
print(guess,"was the number!")
if guess==the_number:
    print("Do you want play again?")
    answer=int(input("Enter 0/1 to continue: "))
    if answer == 0:
        while guess!=the_number:
            if guess>the_number:
                print(guess, "was too high, try again")
            if guess<the_number:
                print(guess,"was too low, try again")
        guess=int(input("Guess again: "))
        print(guess,"was the number!")
    else:
        print("ty for playing!")
        
