import turtle

pencil = turtle.Turtle()
pencil.pensize(1)
pencil.color(0.4, 0.3, 0.6)

length = 150
for _ in range(4):
    for _ in range(4):
        pencil.fd(length)
        pencil.left(90)
    pencil.left(10)


pencil.hideturtle()
pencil.teleport(0, -150)
pencil.write("Squares", align='center', font=('Verdana', 18, 'normal'))

turtle.mainloop()