import turtle

fonts = ["Arial", "Courier", "Comic Sans MS", "Times New Roman", 
         "Verdana", "Tahoma", "Georgia", "Helvetica", "Trebuchet MS"]

start = 250
turtle.up()
turtle.hideturtle()

for font in fonts:
    turtle.goto(0, start)
    turtle.write(font, align='center', font=(font, 22, 'normal'))
    start -= 50

turtle.done()