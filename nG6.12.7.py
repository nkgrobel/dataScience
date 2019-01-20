import turtle
w = turtle.Screen()
w.bgcolor("lightblue")

t = turtle.Turtle()


def draw_square(t, size):
    for i in range(4):
        t.forward(size)
        t.left(90)


size = 20
for j in range(3):
    t.pensize(3)
    draw_square(t, size)
    size = size + 20
    t.penup()
    t.goto(t.pos() + (-10, -10))
    t.pendown()

w.mainloop()
