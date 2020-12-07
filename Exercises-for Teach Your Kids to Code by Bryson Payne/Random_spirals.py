# Random Spirals
import turtle
import random
t=turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors=["red","blue","green","turquoise","white","orange","pink","purple"]
for n in range(50):
    # Generate spirals of random sizes/colors at random location
    t.pencolor(random.choice(colors))             # Pick random color
    size=random.randint(10,40)                    # Random size
    # Generate random spiral position on the screen
    x=random.randrange(-turtle.window_width()//2,turtle.window_width()//2)
    y=random.randrange(-turtle.window_height()//2,turtle.window_height()//2)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)
    
