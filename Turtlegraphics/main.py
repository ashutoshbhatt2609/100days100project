from turtle import Turtle,Screen
from random import choice
t=Turtle()
t.speed(10000000)
t.pensize(10)
color_list=["royal blue","dim gray","dark green","gold","deep pink","orange red","dark olive green","teal"]
s=[90,0,180,270]
def draw():
    c=choice(color_list)
    t.color(c)
    t.forward(30)
    k=choice(s)
    t.right(k)

for i in range(200):
    draw()
scren=Screen()
scren.exitonclick()
