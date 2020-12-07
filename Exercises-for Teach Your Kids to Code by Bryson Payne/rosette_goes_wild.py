# rosette_gone_wild
import turtle
t=turtle.Pen()
turtle.bgcolor("turquoise")
t.pencolor("white")

# ask user imput the number of circles, default to 6
number_of_circles=int(turtle.numinput("Number of circles", "Please enter the number of circles in your rosette", 6))
color=["red", "orange", "white"]

# make loop
for x in range(number_of_circles):
    t.pencolor(color[x%3])
    t.width(5)
    t.circle(100)
    t.left(360/number_of_circles)
    t.circle(70)
    t.left(360/number_of_circles)
    t.circle(40)
    t.left(360/number_of_circles)
    

