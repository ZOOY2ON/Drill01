import turtle

def move_turtle_forward ( ):
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def move_turtle_back ( ):
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.stamp()

def move_turtle_right ( ):
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def move_turtle_left ( ):
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape("turtle")
turtle.stamp()

turtle.onkey(move_turtle_forward, 'w')
turtle.onkey(move_turtle_left, 'a')
turtle.onkey(move_turtle_back, 's')
turtle.onkey(move_turtle_right, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()
