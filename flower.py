import turtle
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.color("magenta")

for i in range(36):
    for j in range(8):
        t.circle(60)
        t.right(45)
    t.right(10)

t.color("yellow")
t.circle(80)

t.hideturtle()
turtle.done()
