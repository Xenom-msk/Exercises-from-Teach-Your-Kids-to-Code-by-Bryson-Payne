# While loop

# Ask user for their name
name=input("What is your name? ")

# Keep printing names until we want to quit
while name != "":
    # Print their name 100 times
    for x in range(100):
        # Print their name followed by a space, not a new line
        print(name, end=" ")
    print()   # After the for loop, skip down to the next line
    name=input("Type another name, or just press [ENTER] to quit: ")
print("Thank you for playing")
