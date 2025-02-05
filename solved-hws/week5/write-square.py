import turtle

pen = turtle.Turtle()
pen.pensize(3)
pen.color('white')
pen.speed(1)
pen.hideturtle()

pencil = turtle.Turtle()
pencil.color('yellow')
pencil.teleport(40, 250)
pencil.hideturtle()

screen = turtle.Screen()
screen.bgcolor('black')

for _ in range(4):
    pen.forward(200)
    pen.left(90)

    pencil.write(f'pen position: ({round(pen.xcor(), 2)},{round(pen.ycor(), 2)})')
    for _ in range(4):
        pen.forward(20)
        pen.left(90)
    pencil.clear()


turtle.done()