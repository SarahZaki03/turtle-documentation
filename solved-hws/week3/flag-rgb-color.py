import turtle

pen = turtle.Turtle()
pen.speed(0)
colors = [(0, 0.6, 0), (1, 1, 0), (1, 0, 0)]

for color in colors:
    pen.pencolor(color)
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(2):
        pen.fd(80)
        pen.right(90)
        pen.fd(200)
        pen.right(90)
    pen.end_fill()

    pen.fd(80)

pen.hideturtle()
pen.teleport(0, 150)
pen.write("Flag", align='center', font=('Verdana', 18, 'normal'))

turtle.done()