# Family spiral
import turtle
t=turtle.Pen()
turtle.bgcolor("black")
colors=["green","red","blue","white","orange","turquoise"]
family=[]   # Set up an empty list for family names

# Ask user to imput first name
name=turtle.textinput("My family","Enter a name, or press [ENTER] to exit: ")

# Keep asking for names
while name !="":
    # Add their name to the family list
    family.append(name)
    # Ask for another name, or finish
    name=turtle.textinput("My family","Enter another name (if you have), or press [ENTER] to exit: ")
# Draw a spiral of the names on the screen
for x in range(100):
    t.pencolor(colors[x%len(family)])   # Rotate through the colors
    t.penup()                           # Dont draw the regular spiral lines
    t.forward(x*4)
    t.pendown()                         # Draw the next family name
    t.write(family[x%len(family)], font=("Arial",int((x+4)/4),"bold"))
    t.left(360/len(family)+2)           # Turn left for our spiral
