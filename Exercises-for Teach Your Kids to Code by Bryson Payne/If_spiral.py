# If spiral
answer=input("Do you want to see a spiral? y/n:")
if answer=='y':
    print("Working...")
    import turtle
    t=turtle.Pen()
    turtle.bgcolor("black")
    t.width(3)
    for x in range(100):
        t.pencolor("white")
        t.forward(x*2)
        t.left(89)
    print("Here is your spiral!")
if answer=='n':
    print("ну и пошел ты, мудила")
