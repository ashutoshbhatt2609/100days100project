import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
scoreboard=Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
CarManager=CarManager()
screen.listen()
screen.onkey(player.go_up,"Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    CarManager.create_car()
    CarManager.move_cars()



    for car in CarManager.all_cars:
        if car.distance(player)<25:
            game_is_on=False
            scoreboard.game_over()
    
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.Increase_level()
   



screen.exitonclick()
