import contextlib

@contextlib.contextmanager
def fill_color(turtle, color):
    turtle.color(color)
    turtle.begin_fill()
    yield 
    turtle.end_fill()