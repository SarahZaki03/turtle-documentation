import turtle

pencil = turtle.Turtle()

screen = turtle.Screen()
screen.listen()

def square():
    length = screen.textinput("Square length", "What is the square length?")
    fill_color = screen.textinput("Square Color", "What is the square fill color?")

    pencil.fillcolor(str(fill_color))
    pencil.begin_fill()
    for _ in range(4):
        pencil.fd(int(length))
        pencil.left(90)
    pencil.end_fill()

def triangle():
    length = screen.textinput("Triangle side length", "What is the triangle side length?")
    fill_color = screen.textinput("Color", "What is the triangle fill color?")
    
    pencil.fillcolor(str(fill_color))
    pencil.begin_fill()
    for _ in range(3):
        pencil.fd(int(length))
        pencil.left(120)
    pencil.end_fill()

def rectangle():
    length = screen.textinput("Rectangle length", "What is the rectangle length?")
    width = screen.textinput("Rectangle width", "What is the rectangle width?")
    fill_color = screen.textinput("Rectangle Color", "What is the rectangle fill color?")
    
    pencil.fillcolor(str(fill_color))
    pencil.begin_fill()
    for _ in range(2):
        pencil.fd(int(length))
        pencil.left(90)
        pencil.fd(int(width))
        pencil.left(90)
    pencil.end_fill()

turtle.onkey(square, 's')
turtle.onkey(rectangle, 'r')
turtle.onkey(triangle, 't')
turtle.onkey(pencil.clear, ' ')
turtle.mainloop()