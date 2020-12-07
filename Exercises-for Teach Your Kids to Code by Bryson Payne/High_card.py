# High card
import random
suits=["diamonds", "hearts", "clubs", "spades"]
faces=["2","3","4","5","6","7","8","9","10","jack","queen","king","ace"]
keep_going=True
while keep_going:
    my_face=random.choice(faces)
    my_suit=random.choice(suits)
    computer_face=random.choice(faces)
    computer_suit=random.choice(suits)
    print("My card is",my_face,"of the",my_suit+".")
    print("Computer card is",computer_face,"of the",computer_suit+".") # Поставил в конце так чтобы была точка в конце предлоджения, инче никак.
    if faces.index(my_face)>faces.index(computer_face):
        print("I win!")
    elif faces.index(my_face)<faces.index(computer_face):
        print("Computer wins")
    else:
        print("Draw")
    answer=input("Do you want play again? Press [Y] to keep going: ").upper()
    keep_going=(answer=="Y")
