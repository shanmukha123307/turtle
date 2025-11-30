import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(300, 400)
polygon = turtle.Turtle()
polygon.color("yellow")

num_sides = 6
length = 60
angle = 360/num_sides
for i in range(num_sides):
    polygon.forward(length)
    polygon.right(angle)

turtle.done()
