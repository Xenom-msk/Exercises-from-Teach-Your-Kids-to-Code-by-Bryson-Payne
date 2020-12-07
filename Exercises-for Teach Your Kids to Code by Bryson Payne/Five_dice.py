# Five dice
# Yahtzee - all five dice are the same
import random
# Game loop
keep_going=True
while keep_going:
                                  # Roll five random dice
    dice=[0,0,0,0,0]              # Set up a array for five values dice[0]-[4]
    for i in range(5):            # Roll a random number from 1-6 for all 5 dice
        dice[i]=random.randint(1,6)
    print("You rolled:",dice)     # Print out the dice values
    dice.sort()                   # Sort them
                                  # Check for five of a kind, four of a kind and three of a kind
    if (dice[0]==dice[4]):
        print("Yahtzee!")
        # Специально добавил, чтобы программа кончалась, когда наролю 6 из 6
        keep_going=input("Do you want continue? Press [any button] to play again, or [enter] to quit: ").lower()
    elif (dice[0]==dice[3]) or (dice[1]==dice[4]):
        print("Four of a kind!")
    elif (dice[0]==dice[2]) or (dice[1]==dice[3]) or (dice[2]==dice[4]):
        print("Three of a kind!")
    # Если добавить строку снизу, то после каждого раза нужно повторять
    # keep_going=input("Do you want continue? Press [y] to play again: ").lower()
    

    
    

