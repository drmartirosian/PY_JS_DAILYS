import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
#==================SCREEN_STTINGS====================================#
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
#=======================PLYR_SETUP===============================#
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
#==============================CARS=================================#

screen.listen()
screen.onkey(player.go_up,'Up')
#======================RUN_GAME================================#
game_is_on = True #RUN GAME
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car() #MAKE CARS

    car_manager.move_cars() #CAR LIST

    if player.ycor() == 280: #DETECT IF PLYR CROSSES
        player.goto(0,-280)
        scoreboard.increment_level()
        car_manager.increase_car_speed()

    for car in car_manager.all_cars: #IF HIT BY CAR
        if car.distance(player) < 20:
            scoreboard.reset_score()
            player.goto(0,-280)
            car_manager.car_speed = 5
#======================================================#