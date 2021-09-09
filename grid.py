import turtle

count = 12
while (count>6):
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.left(180)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    count -= 1

turtle.right(90)
turtle.forward(600)
turtle.left(180)
    
while (count>0):
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.left(180)
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    count -= 1

turtle.exitonclick()
