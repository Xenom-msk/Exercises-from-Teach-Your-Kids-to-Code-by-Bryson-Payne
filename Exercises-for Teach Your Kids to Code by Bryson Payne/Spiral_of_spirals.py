# Viral spiral
import turtle
t=turtle.Pen()
turtle.bgcolor("black")
t.penup()

# Ask the user for the number of sides, default 4, min 2, max 6
sides=int(turtle.numinput("Number of sides","How many sides do you want (2-6)?",4,2,6))
color=["white","red","blue","orange","pink","brown"]

# Make our outer spiral loop
for m in range (100):
    t.forward(m*4)
    position=t.position()
    heading=t.heading()
    # Make our inner spiral loop
    for n in range(int(m/2)):
                   t.pendown()
                   t.pencolor(color[n%sides])
                   t.forward(n*2)
                   t.right(360/sides-2)
                   t.penup()
    t.setx(position[0])       # Go back to the big spiral's x location
    t.sety(position[1])       # Go back to the big spiral's y location
    t.setheading(heading)     # Point in the big spiral's heading
    t.left(360/sides+2)       # Aim at the next point on the big spiral
