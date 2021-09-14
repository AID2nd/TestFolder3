import turtle

def turtle_moveup():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def turtle_moveleft():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def turtle_movedown():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def turtle_moveright():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(turtle_moveup, 'w')
turtle.onkey(turtle_moveleft, 'a')
turtle.onkey(turtle_movedown, 's')
turtle.onkey(turtle_moveright, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()
turtle.exitonclick()


