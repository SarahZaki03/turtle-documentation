import turtle
import random
pen = turtle.Turtle()

pen.speed(0)
pen.pensize(3)

colors = ['yellow', 'blue', 'red', 'orange', 'purple', 'green']

for i in range(300):
    pen.color(colors[i%len(colors)])

    # Select Random number from the list --------
    # pen.color(random.choice(colors))
    # -------------------------------------------

    pen.forward(0.1+i*0.1)
    pen.right(10)

turtle.done()