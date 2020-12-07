# Color spiral input
import turtle
t=turtle.Pen()
turtle.bgcolor("black")

# Set up a list of any 8 color names
colors=["red", "green", "blue", "yellow", "orange", "pink", "white", "purple"]

#Ask the user for the number of sides, betwen 1 and 8, with default of 4
sides=8

# Draw a colorful spiral with the user-specified number of sides
for x in range(360):
    t.pencolor(colors[x%sides])    # Only use the right number of colors
    t.forward(x*3/sides+x)                 # Change the size to match the number of sides
    t.left(360/sides+1)            # Turn 360 degrees / number of sides, plus 2
    t.width(x*sides/200)                     # Make the pen larger as it goes outward
