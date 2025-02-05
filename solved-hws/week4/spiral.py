import turtle

pen = turtle.Turtle()

colors = ['yellow', 'blue', 'red', 'orange', 'purple', 'green']
print(colors[1]) # Yellow (index, position, address) We start from zero
print(colors[5]) # Green


# variables -----------
length = 10 
thickness = 1  

for i in range(50):
    pen.color(colors[i % 6])
    pen.pensize(thickness)
    pen.fd(length)
    pen.left(45)
    thickness += 0.4
    length += 3

turtle.done()