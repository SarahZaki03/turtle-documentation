#Join The Dots Challenge - www.101computing.net/join-the-dots-challenge/
import turtle
screen = turtle.Screen()

# this assures that the size of the screen will always be 400x400 ...
screen.setup(500, 500)

pen = turtle.Turtle()
pen.shape("circle")
pen.speed(100)
pen.color("#810081")
pen.pensize(6)
pen.penup()

#Draw the 9 dots
for i in range(0,9):
   x = i % 3
   y = i // 3
   pen.goto(-100+x*100, -100+y*100)
   pen.stamp()

#Starting Position
pen.goto(-100,-100)

pen.pendown()
pen.goto(100,100)
#Continue the code here...
pen.goto(-200,100)
pen.goto(100,-200)
pen.goto(100,100)

turtle.done()