import turtle

def make_turtle(shape, speed, color, fillcolor, pensize):
    pencil = turtle.Turtle(shape)
    pencil.speed(speed)
    pencil.pencolor(color)
    pencil.fillcolor(fillcolor)
    pencil.pensize(pensize)
    return pencil

def make_screen(title, bgcolor, width, height):
    screen = turtle.Screen()
    screen.title(title)
    screen.bgcolor(bgcolor)
    screen.setup(width, height)

s = make_screen('title', 'lightblue', 500, 500)
t = make_turtle('circle', 0, 'green', 'pink', 4)

t.fd(100)
turtle.done()