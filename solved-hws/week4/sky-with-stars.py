import turtle
import random

pen = turtle.Turtle()

pen.hideturtle()
pen.speed(0)

# create my screen ------
screen = turtle.Screen()
screen.bgcolor('black')


for i in range(100): 
    pen.dot(random.randint(2, 4), 'yellow') # draw small dot, color: yellow
    pen.up()
    x = random.randint(-400, 400) # -400 ------> 400
    y = random.randint(-400, 400)
    pen.goto(x, y)


x = 0
y = 150
pen.goto(x, y)
pen.color('white')
pen.down()
pen.fillcolor()
pen.begin_fill()
pen.circle(40)
pen.end_fill()

turtle.done()