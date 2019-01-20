# Extend your program above. Draw five stars,
# but between each, pick up the pen, move forward by 350 units, turn
# right by 144, put the pen down, and draw the next star.
# You’ll get something like this (note that you will need to move to the left before
# drawing your first star in order to fit everything in the window)
import turtle
t = turtle.Turtle()
w = turtle.Screen()
w.bgcolor("lightgreen")


def stars():
    t.color("violet")
    t.penup()
    t.forward(-160)
    t.pendown()
    for i in range(5):
        star()
        t.penup()
        t.forward(350)
        t.right(144)
        t.pendown()


def star(n=5):
    for i in range(n):
        t.forward(100)
        t.right(180-180.0/n)


stars()
w.exitonclick()

