# Random Spirals Function
import turtle
import random
t=turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors=["red","blue","green","turquoise","white","orange","pink","purple"]
def random_spiral():
    t.pencolor(random.choice(colors))
    size=random.randint(10,40)
    x=random.randrange(-turtle.window_width()//2,turtle.window_width()//2)
    y=random.randrange(-turtle.window_height()//2,turtle.window_height()//2)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)

for n in range(50):
    random_spiral()
    
