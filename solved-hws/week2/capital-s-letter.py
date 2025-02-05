import turtle

pencil = turtle.Turtle()
pencil.pensize(3)
pencil.color(0.4, 0.3, 0.6)


pencil.teleport(0, 50)
pencil.left(140)
pencil.circle(50, 200)
pencil.fd(30)
# pencil.left(140)
pencil.circle(-50, 240)

pencil.hideturtle()

pencil.teleport(0, 150)
pencil.write("Capital S letter", align='center', font=('Verdana', 18, 'normal'))

turtle.mainloop()