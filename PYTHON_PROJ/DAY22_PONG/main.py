from turtle import Screen, Turtle
from random import random, randint
from paddle import Paddle
#============================SCREEN SETTINGS======================#
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600) 
screen.title('PONG')
screen.tracer(0)


#============================START===============================#
#MAKE BOTH PADDLES
right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))

#Move paddle
screen.listen()
screen.onkey(left_paddle.go_up,"Up")
screen.onkey(left_paddle.go_down,"Down")

#UPDATE SCREEN
game_is_on = True
while game_is_on == True:
    screen.update()


#=============================END================================#
screen.exitonclick()