import turtle

pen = turtle.Turtle()
pen.pensize(3)
pen.color('red')

for _ in range(8):
    pen.fd(100)
    pen.back(100)
    pen.right(45)

pen.hideturtle()


pencil = turtle.Turtle()
pencil.hideturtle()
def write_word():
    pencil.up()
    pencil.goto(0, -200)
    pencil.write("Asterisk", align='center', font=('Georgia', 22, 'normal'))
    turtle.ontimer(write_word, 2000)

def clear_word():
    pencil.clear()
    turtle.ontimer(clear_word, 2000)

turtle.ontimer(write_word, 2000)
turtle.ontimer(clear_word, 2000)

turtle.mainloop()