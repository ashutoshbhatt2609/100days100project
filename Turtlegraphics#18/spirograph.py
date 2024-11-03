import turtle as t 
from random import *
ti=t.Turtle()
ti.speed("fastest")
t.colormode(255)
def random_color():
    r=randint(0,255)
    b=randint(0,255)
    g=randint(0,255)
    return(r,b,g)
for i in range (360):
    ti.color(random_color())
    ti.circle(200)
    #ti.left(angle=1) This also works !!!!!!!!!
    ti.setheading(ti.heading()+1)
scr=t.Screen()
scr.exitonclick()