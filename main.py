import turtle

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.speed(0)
turtle.tracer(3,0)
t.color("#D7CCC8")
for i in range(600):
    t.forward(i)
    t.left(170)
    t.forward(i)
    t.left(45)
turtle.done()
