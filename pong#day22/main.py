from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scorecard import Scoreboard


import time
srn=Screen()
game_ball=Ball()
scoreboard_1=Scoreboard()
srn.setup(width=800, height=600)
srn.bgcolor("black")
srn.title("Pong Game")
srn.tracer(0)
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

srn.listen()
srn.onkey(r_paddle.go_up,"Up")
srn.onkey(r_paddle.go_down,"Down")
srn.onkey(l_paddle.go_up,"w")
srn.onkey(l_paddle.go_down,"s")


game_is_on=True
while game_is_on:
    time.sleep(game_ball.move_speed)
    srn.update()
    game_ball.move()
    if game_ball.ycor()>280 or game_ball.ycor()<-280:
        game_ball.bounce_y()

     
    if game_ball.distance(r_paddle)<50 and (game_ball.xcor()>330 and game_ball.xcor()<360) or game_ball.distance(l_paddle)<50 and (game_ball.xcor()<-330 and game_ball.xcor()>-360):
        game_ball.bounce_x()
    
    if game_ball.xcor()>380:
        game_ball.reset_position()
        scoreboard_1.l_point()
        

    if game_ball.xcor()<-380:
        game_ball.reset_position()
        scoreboard_1.r_point()
    



   

    
    


























srn.exitonclick()