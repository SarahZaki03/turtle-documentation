import turtle

pen = turtle.Turtle()
colors = [(0, 0.6, 0), (1, 1, 0), (1, 0, 0)]
pen.teleport(-150, 150)
pen.speed(0)

for color in colors:
    pen.pencolor(color)
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(2):
        pen.fd(300)
        pen.right(90)
        pen.fd(80)
        pen.right(90)
    pen.end_fill()

    pen.right(90)
    pen.fd(80)
    pen.left(90)

pen.hideturtle()
pen.teleport(0, 200)
pen.write("Flag", align='center', font=('Verdana', 18, 'normal'))
pen.teleport(-5, 22)

pen.fillcolor('red')
pen.begin_fill()
for _ in range(5):
    pen.right(72)
    pen.fd(30)
    pen.left(144)
    pen.fd(30)
pen.end_fill()


turtle.done()