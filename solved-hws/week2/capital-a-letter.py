import turtle

pencil = turtle.Turtle()
pencil.pensize(3)
pencil.color(0.6, 0.4, 0.4)

# Drawing Capital a letter using goto -------
pencil.teleport(-50, 0)
pencil.goto(0, 100)
pencil.goto(50, 0)
pencil.teleport(30 ,40)
pencil.goto(-30, 40)

# Drawing Capital a letter using forward-backward-left-right -------
pencil.teleport(0, 0)
pencil.up()
pencil.backward(100)
pencil.down()
pencil.left(60)
pencil.fd(200)
pencil.right(120)
pencil.fd(200)

pencil.back(100)
pencil.right(120)
pencil.fd(100)
pencil.hideturtle()


pencil.up()
pencil.goto(0, -100)
pencil.write("Capital A letter Using Goto - Teleport", 
             align='center', font=('Verdana', 18, 'normal'))

pencil.goto(0, -150)
pencil.write("Capital A letter Using Forward - Backward - Right - Left", 
             align='center', font=('Verdana', 18, 'normal'))

turtle.mainloop()