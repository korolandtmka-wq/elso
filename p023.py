import turtle

def haromszog():
    turtle.pencolor("red")
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(-75, -37.5)
    turtle.pendown()

    for i in range(3):
        turtle.forward(150)
        turtle.left(120)

    turtle.hideturtle()

def pont(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def inditas():
    turtle.clear()
    haromszog()



#applikáció
ablak = turtle.Screen()
ablak.bgcolor("gray")

turtle.onkey(inditas, "h")
turtle.listen()
turtle.onkey(turtle.bye, "q")
turtle.mainloop()