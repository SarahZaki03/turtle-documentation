import turtle

turtle.tracer(0, 0)
pen = turtle.Turtle()
pen.pensize(3)

pen.teleport(0, -100)
pen.circle(200)

pen.circle(200, 90)


# Draw the red half of the design ----------
pen.fillcolor('red')
pen.begin_fill()
pen.circle(200, 180)
pen.seth(0)
pen.pensize(7)
pen.forward(400)
pen.end_fill()
# -----------------------------------------

pen.teleport(0, 40)
pen.seth(0)
pen.fillcolor('white')
pen.begin_fill()
pen.circle(60)
pen.end_fill()


pen.teleport(0, 75)
pen.circle(25)

pen.hideturtle()

turtle.update()
turtle.done()