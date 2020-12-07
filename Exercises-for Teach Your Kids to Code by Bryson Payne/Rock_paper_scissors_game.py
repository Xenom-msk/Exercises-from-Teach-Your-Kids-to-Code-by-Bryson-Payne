# Rock, paper, scissors game
import random
choices=["rock","paper","scissors"]
print("Rock crushes scissors. Scissors cut paper. Paper covers rock.")
player=input("Do you want be rock, paper or scissors (or quit [press q])? ").lower()
while player !="q":                    # Keep playing until the user quits
    computer=random.choice(choices)    # Pick one of the items in choise
    print("You chose "+player+", and the computer chose "+computer+".")
    if player==computer:
        print("Draw")
    elif player=="rock":
        if computer=="scissors":
            print("You beat the scissors with rock")
        else:
            print("You lose")
    elif player=="scissors":
        if computer=="paper":
            print("You win!")
        else:
            print("You lose")
    elif player=="paper":
        if computer=="rock":
            print("You cover rock with paper")
        else:
            print("You lose")
    else:
        print("There was some error in your input...")
    print()
    player=input("Do you want play again? ")
