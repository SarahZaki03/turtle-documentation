import turtle

pencil = turtle.Turtle()
pencil.pensize(1)
pencil.color(0.4, 0.3, 0.6)
pencil.speed(0)
pencil.back(100)

point = 10
length = 200
for _ in range(6):
    for _ in range(4):
        pencil.fd(length)
        pencil.left(90)
    pencil.teleport(point-100, point)
    length -= 20; point += 10


pencil.hideturtle()
pencil.teleport(0, -150)


pencil.write("Overlapping Squares", align='center', font=('Verdana', 18, 'normal'))

turtle.mainloop()