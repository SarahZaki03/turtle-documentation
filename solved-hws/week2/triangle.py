import turtle

pencil = turtle.Turtle()
pencil.pensize(3)
pencil.color(0.3, 0.1, 0.6)


triangle_sides = 3

for _ in range(triangle_sides):
    pencil.fd(70)
    pencil.left(360/triangle_sides)


turtle.mainloop()