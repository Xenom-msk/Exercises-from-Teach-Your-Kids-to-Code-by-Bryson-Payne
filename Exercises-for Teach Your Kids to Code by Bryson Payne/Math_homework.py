# Math homework
print("Math homework")

# Ask user to enter the math problem
problem=input("Enter the math problem, or 'q' to quit: ")
colors=["red", "green"]
textcolor(colors[x%2])

# Keep going until the user press 'q' to quit
while(problem !="q"):
    # Show the problem and the answer using eval()
    print("The answer to ", problem, "is", eval(problem))
    # Ask for another math problem
    problem=input("Enter another math problem, or 'q' to quit: ")
    # This while loop will keep going until you enter 'q' to quit
