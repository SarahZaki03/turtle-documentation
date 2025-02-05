import turtle

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)

# Draw first big Triangle -----------
for distance in [300, 200, 300, 200]:
    pen.forward(distance)
    pen.left(90)
# -----------------------------------


# Draw the door for the home --------
pen.goto(130, 0)
for distance in [40, 70, 40, 70]:
    pen.forward(distance)
    pen.left(90)
# -----------------------------------


# Draw the triangle above the home --
pen.teleport(300, 200)
pen.left(146)
pen.fd(180)
pen.goto(0, 200)
# -----------------------------------

pen.seth(0)
# Draw the windows ------------------
# Window 1 --------------------------
pen.teleport(30, 100)
for i in range(4):
    pen.fd(40)
    pen.left(90)

pen.fd(20)
pen.left(90)
pen.fd(40)
pen.left(90)
pen.fd(20)
pen.left(90)
pen.fd(20)
pen.left(90)
pen.fd(40)

# Window 2 --------------------------
pen.teleport(130, 100)
for i in range(4):
    pen.fd(40)
    pen.left(90)

pen.fd(20)
pen.left(90)
pen.fd(40)
pen.left(90)
pen.fd(20)
pen.left(90)
pen.fd(20)
pen.left(90)
pen.fd(40)

# Window 3 --------------------------
pen.teleport(230, 100)
for i in range(4):
    pen.fd(40)
    pen.left(90)

pen.fd(20)
pen.left(90)
pen.fd(40)
pen.left(90)
pen.fd(20)
pen.left(90)
pen.fd(20)
pen.left(90)
pen.fd(40)
# -----------------------------------
pen.hideturtle()

turtle.done()