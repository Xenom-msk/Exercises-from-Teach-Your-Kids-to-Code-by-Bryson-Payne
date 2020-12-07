# Rossetes and polygons
import turtle
t=turtle.Pen()
turtle.bgcolor("turquoise")
sides=int(turtle.numinput("Number of sides", "Please enter number of sides",4))
# Our outer spiral loop for polygons and rosettes, from size 5 to 75
for m in range(5,75):
    t.left(360/sides+5)
    t.width(m//25+1)
    t.penup()
    t.forward(m*4)
    t.pendown()
    # Draw a little rosette at each EVEN corner of the spiral
    if(m%2==0):
        for n in range(sides):
            t.pencolor("white")
            t.circle(m/3)
            t.right(360/sides)
    # Or draw a little polygon at each ODD corner of the spiral
    else:
        for n in range(sides):
            t.pencolor("black")
            t.forward(m)
            t.right(360/sides)
