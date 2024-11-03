from turtle import Turtle,Screen

t=Turtle()
srn=Screen()
def move_forward():
    t.fd(10)
def move_backward():
    t.backward(10)
def move_left():
    t.lt(5)
def move_right():
    t.rt(5)
def clear():
    t.clear()
    t.pu()
    t.home()
    t.pd()
srn.listen()
srn.onkey(key="w",fun=move_forward)#we dont add paranthesis coz it trigers the function there itself
srn.onkey(key="s",fun=move_backward)#we dont add paranthesis coz it trigers the function there itself
srn.onkey(key="a",fun=move_left)#we dont add paranthesis coz it trigers the function there itself
srn.onkey(key="d",fun=move_right)#we dont add paranthesis coz it trigers the function there itself
srn.onkey(key="c",fun=clear)#we dont add paranthesis coz it trigers the function there itself


srn.exitonclick()
