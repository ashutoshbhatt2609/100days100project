from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
srn=Screen()
game_ball=Ball()
srn.setup(width=800, height=600)
srn.bgcolor("black")
srn.title("Pong Game")
srn.tracer(0)
l_paddle=Paddle((350,0))
r_paddle=Paddle((-350,0))

srn.listen()
srn.onkey(l_paddle.go_up,"Up")
srn.onkey(l_paddle.go_down,"Down")
srn.onkey(r_paddle.go_up,"w")
srn.onkey(r_paddle.go_down,"s")


game_is_on=True
while game_is_on:
    time.sleep(0.1)
    srn.update()
    game_ball.move()



























srn.exitonclick()