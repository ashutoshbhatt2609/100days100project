import turtle
from random import choice,randint
t=turtle.Turtle()
turtle.colormode(255)
t.speed(10000000)
t.pensize(10)
def random_color():
    r=randint(0,255)
    b=randint(0,255)
    g=randint(0,255)
    return(r,b,g)
s=[90,0,180,270]
def draw():
    t.color(random_color())
    t.forward(30)
    k=choice(s)
    t.right(k)

for i in range(200):
    draw()
scren=turtle.Screen()
scren.exitonclick()
