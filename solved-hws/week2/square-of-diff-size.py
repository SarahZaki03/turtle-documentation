import turtle

pencil = turtle.Turtle()
pencil.pensize(3)
pencil.color(0.4, 0.3, 0.6)

length = 50
for _ in range(4):
    for _ in range(4):
        pencil.fd(length)
        pencil.left(90)
    length += 20


pencil.hideturtle()

pencil.teleport(0, -150)
pencil.write("Squares of different sizes", align='center', font=('Verdana', 18, 'normal'))

turtle.mainloop()