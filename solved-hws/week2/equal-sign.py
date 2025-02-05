import turtle


pen = turtle.Turtle()
pen.pensize(3)
# pen.hideturtle()

# Equal sign
pen.backward(100)
pen.forward(200)
pen.left(90)

pen.up()
pen.forward(50)
pen.down()

pen.left(90)
pen.forward(200)

pen.hideturtle()

pen.up()
pen.goto(0, -100)
pen.write("Equal Sign", align='center', font=('Georgia', 22, 'normal'))

turtle.done()