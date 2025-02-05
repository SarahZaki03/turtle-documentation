import turtle
import fillcolor as fc


pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)

screen = turtle.Screen()
screen.bgcolor('navy')

# pen.color('orange')
# pen.begin_fill()
# pen.circle(100)
# pen.end_fill()

with fc.fill_color(pen, 'orange'):
    pen.circle(100)

pen.up()
pen.forward(20)
pen.down()

with fc.fill_color(pen, 'navy'):
    pen.circle(100)

pen.hideturtle()

turtle.done()