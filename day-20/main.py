from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("The snake game!!")
screen.tracer(0)
snake=Snake()

food=Food()
score=Scoreboard()




screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collission of food
    if snake.head.distance(food)<15:
        snake.extend()
        food.refresh()
        score.increase_score()
    #detect collission with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        score.reset()
        snake.reset()

    #detect collission with tail
    for segment in snake.segments[1:]:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            score.reset()
            snake.reset()
            



screen.exitonclick()


