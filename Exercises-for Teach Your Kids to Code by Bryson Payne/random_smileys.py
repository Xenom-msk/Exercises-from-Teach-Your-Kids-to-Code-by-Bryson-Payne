# Random smileys
import random
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
t.hideturtle()
x=1
y=1
def draw_smiley(x,y):
    for b in range(50):
        t.penup()
        t.setpos(x,y)
        t.pendown()
        # Head
        t.pencolor("white")
        t.fillcolor("white")
        t.begin_fill()
        t.circle(50)
        t.end_fill()  
        # Left eye
        t.setpos(x-15, y+60)
        t.fillcolor("black")
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        # Right eye
        t.setpos(x+15, y+60)
        t.fillcolor("black")
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        # Mouth
        t.setpos(x-25, y+40)
        t.pencolor("black")
        t.width(10)
        t.fillcolor("black")
        t.begin_fill()
        t.goto(x-10, y+20)
        t.goto(x+10, y+20)
        t.goto(x+25, y+40)
        t.goto(x-25, y+40)
        t.end_fill()
        t.width(1)
        # Left Fang
        t.setpos(x-17,y+45)
        t.pencolor("white")
        t.fillcolor("white")
        t.begin_fill()
        t.goto(x-15,y+37)
        t.goto(x-13,y+45)
        t.end_fill()
        # Right Fang
        t.setpos(x+17,y+45)
        t.pencolor("white")
        t.fillcolor("white")
        t.begin_fill()
        t.goto(x+15,y+37)
        t.goto(x+13,y+45)
        t.end_fill()
        for n in range(50):
            x=random.randrange(-turtle.window_width()//2,turtle.window_width()//2)
            y=random.randrange(-turtle.window_height()//2,turtle.window_height()//2)

for z in range(1):
    draw_smiley(x,y)
