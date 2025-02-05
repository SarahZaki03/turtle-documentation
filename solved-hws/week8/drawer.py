import turtle

screen = turtle.Screen()
screen.bgcolor('pink')
screen.title("Drawer")
screen.listen()

pen = turtle.Turtle()
pen.pensize(3)

def right():
    pen.seth(0)
    pen.fd(20)

def left():
    pen.seth(180)
    pen.fd(20)

def up():
    pen.seth(90)
    pen.fd(20)

def down():
    pen.seth(270)
    pen.fd(20)

def turn_right():
    angle = pen.heading()
    pen.seth(angle+5)

def turn_left():
    angle = pen.heading()
    pen.seth(angle-5)

def forward():
    pen.forward(10)

turtle.onkey(right  , 'Right')
turtle.onkey(left, 'Left' )
turtle.onkey(up , 'Up'   )
turtle.onkey(down, 'Down' )
turtle.onkey(forward   , 'f')
turtle.onkey(pen.home  , '0')
turtle.onkey(pen.clear , ' ')
turtle.onkey(turn_right, '+')
turtle.onkey(turn_left , '-')

# need for search by student -------------------------
turtle.onkey(pen.undo, 'u')

turtle.done()