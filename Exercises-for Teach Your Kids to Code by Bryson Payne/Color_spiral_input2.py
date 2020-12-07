# Color Spiral Input
import turtle
t=turtle.Pen()
turtle.bgcolor("black")

sides=8
for x in range(100):
    t.pencolor("white")
    t.forward(x+1)
    t.left(80)
    t.width(x)
