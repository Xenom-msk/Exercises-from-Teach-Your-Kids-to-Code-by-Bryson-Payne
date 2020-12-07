# Spiral name
import turtle  # Set up turtle graphics
t=turtle.Pen()
turtle.bgcolor("black")
colors=["red", "green", "blue", "yellow"]

#Ask the user his name
your_name=turtle.textinput("Enter your name", "What is your name? ")
                           
#Draw a spiral name on the screen, written 100 times
for x in range(100):
                           t.pencolor(colors[x%4])  # Rotate through the four colors
                           t.penup()                # Dont draw the regular spiral lines
                           t.forward(x*4)           # Move turtle forward on x pixels
                           t.pendown()              # Whrite name bigger each time
                           t.write(your_name, font=("Comic Sans MS", int((x+4)/4), "bold"))
                           t.left(92)               # Turn left, just as in our other spirals
                           
