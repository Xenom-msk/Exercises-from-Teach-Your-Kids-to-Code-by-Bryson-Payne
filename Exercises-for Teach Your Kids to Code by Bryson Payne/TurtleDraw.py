# Color Spiral
import turtle
t=turtle.Pen()
turtle.bgcolor("black")
sides=eval(input("введите число сторон от 2 до 10: "))
colors=["green", "red", "blue", "yellow", "white", "orange", "purple", "pink", "turquoise", "lemon chiffon"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x*3)
    t.left(360/sides+1)
    t.width(20)
    t.left(90)
