import turtle

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)

def move_to(x, y):
    pen.teleport(x, y)

def draw_square(x, y, length):
    move_to(x, y)
    for _ in range(4):
        pen.forward(length)
        pen.left(90)

def draw_rectangle(x, y, length, width):
    move_to(x, y)
    for _ in range(2):
        pen.forward(length)
        pen.left(90)
        pen.forward(width)
        pen.left(90)

# Draw first big Triangle -----------
draw_rectangle(0, 0, 300, 200)
# -----------------------------------

# Draw the door for the home --------
draw_rectangle(130, 0, 40, 70)
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
draw_square(30, 100, 40)

for step in [20, 40, 20, 20, 40]:
    pen.fd(step)
    pen.left(90)
pen.right(90)

# Window 2 --------------------------
draw_square(130, 100, 40)

for step in [20, 40, 20, 20, 40]:
    pen.fd(step)
    pen.left(90)
pen.right(90)

# Window 3 --------------------------
draw_square(230, 100, 40)

for step in [20, 40, 20, 20, 40]:
    pen.fd(step)
    pen.left(90)
# -----------------------------------
pen.hideturtle()

turtle.done()