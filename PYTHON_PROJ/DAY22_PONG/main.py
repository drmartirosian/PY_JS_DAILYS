from turtle import Screen, Turtle
from random import random, randint
from paddle import Paddle
from ball import Ball
import time 
#============================SCREEN SETTINGS======================#
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600) 
screen.title('PONG')
screen.tracer(0)


#============================START===============================#
#MAKE BOTH PADDLES
left_paddle = Paddle((350,0))
right_paddle = Paddle((-350,0))
ball = Ball()

#Move paddle
screen.listen()
#PLAYER1
screen.onkey(right_paddle.go_up,"w")
screen.onkey(right_paddle.go_down,"s")
#PLAYER2
screen.onkey(left_paddle.go_up,"Up")
screen.onkey(left_paddle.go_down,"Down")

#UPDATE SCREEN
game_is_on = True
while game_is_on == True:
    time.sleep(0.1)#slow things down slightly
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    





#=============================END================================#
screen.exitonclick()