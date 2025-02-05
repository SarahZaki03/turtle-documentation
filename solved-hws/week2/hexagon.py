import turtle

pencil = turtle.Turtle()
pencil.pensize(3)
pencil.color(0.3, 0.1, 0.6)


hexagon_sides = 6

for _ in range(hexagon_sides):
    pencil.fd(70)
    pencil.left(360/hexagon_sides)

pencil.left(90)
pencil.color('navy')
# build hexagon using circle method -------
pencil.circle(70, 360, 6)


turtle.mainloop()