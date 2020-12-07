import turtle
import random
t=turtle.Pen()
turtle.bgcolor("Black")
t.speed(0)
colors=["red","white","blue","green","pink","orange","yellow","purple","turquoise"]

def spiral(x,y):
    t.pencolor(random.choice(colors))
    size=random.randint(10,40)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)
turtle.onscreenclick(spiral)
