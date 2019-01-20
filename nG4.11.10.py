import turtle
w = turtle.Screen()
w.bgcolor('teal')
t = turtle.Turtle()
t.color('blue')
t.shape('turtle')
t.stamp()
move = 30
for i in range(12):
    t.penup()
    t.forward(60)
    t.pendown()
    t.forward(30)
    t.penup()
    t.forward(20)
    t.stamp()
    t.home()
    t.right(move)
    move = move+30
w.exitonclick()

