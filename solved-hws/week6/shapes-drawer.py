import turtle

pencil = turtle.Turtle()

screen = turtle.Screen()
screen.listen()

def square():
    for _ in range(4):
        pencil.fd(100)
        pencil.left(90)

def triangle():
    for _ in range(3):
        pencil.fd(100)
        pencil.left(120)

def rectangle():
    for _ in range(2):
        pencil.fd(200)
        pencil.left(90)
        pencil.fd(100)
        pencil.left(90)


turtle.onkey(square, 's')
turtle.onkey(rectangle, 'r')
turtle.onkey(triangle, 't')
turtle.onkey(pencil.clear, ' ')
turtle.mainloop()