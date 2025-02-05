import turtle

screen = turtle.Screen()
screen.bgcolor('pink')
screen.title("Drawer")
screen.listen()

pen = turtle.Turtle()
pen.pensize(3)

def change_head_move(direction):
    """Move the turtle into the desired Direction"""
    pen.seth(direction)
    pen.fd(20)

def turn_right():
    angle = pen.heading()
    pen.seth(angle+5)

def turn_left():
    angle = pen.heading()
    pen.seth(angle-5)

def forward():
    pen.forward(10)

turtle.onkey(lambda: change_head_move(0)  , 'Right')
turtle.onkey(lambda: change_head_move(180), 'Left' )
turtle.onkey(lambda: change_head_move(90) , 'Up'   )
turtle.onkey(lambda: change_head_move(270), 'Down' )
turtle.onkey(forward   , 'f')
turtle.onkey(pen.home  , '0')
turtle.onkey(pen.clear , ' ')
turtle.onkey(turn_right, '+')
turtle.onkey(turn_left , '-')

# need for search by student -------------------------
turtle.onkey(pen.undo, 'u')

turtle.done()