# Polygon or rosette
import turtle
t=turtle.Pen()
turtle.bgcolor("black")
t.pencolor("white")
# Aks user for the number of sides, default to 6
number=int(turtle.numinput("Number of sides or circles","How many sides do you want in your shape?",6))
# Aks user whether they want a polygon or roserre
shape=turtle.textinput("What kind of shape do you want?", "Enter 'p' for polygon or 'r' for rossete:")
for x in range(number):
    if shape=='p':     # User selected polygon
        t.forward(100)
        t.left(35)
    else:
        t.circle(100)
    t.left(360/number)
