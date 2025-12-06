import turtle
screen = turtle.Screen()
screen.bgcolor("lightblue")
t = turtle.Turtle()
t.pensize(4)
t.color("red")   
t.speed(3)
for _ in range(4):
    t.forward(100)
    t.right(90)

turtle.done()
