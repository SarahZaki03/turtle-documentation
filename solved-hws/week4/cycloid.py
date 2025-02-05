import turtle
import math

radius = 20

for i in range(0, 300):
    step = i * 0.1
    x = radius * (step - math.sin(step))
    y = radius * (1 - math.cos(step))
    turtle.goto(x, y)


turtle.done()