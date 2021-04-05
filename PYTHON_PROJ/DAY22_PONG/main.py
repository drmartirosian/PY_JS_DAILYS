from turtle import Screen, Turtle
from random import random, randint
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time 
#============================SCREEN SETTINGS======================#
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600) 
screen.title('PONG')
screen.tracer(0)


#============================START===============================#
#MAKE BALL
ball = Ball()
#MAKE SCOREBOARD
scoreboard = Scoreboard()
#MAKE BOTH PADDLES
l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
#Move BOTH paddle
screen.listen()
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

#UPDATE SCREEN
game_is_on = True
while game_is_on == True:
    time.sleep(0.1)#slow things down slightly
    screen.update()
    ball.move()
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #IF BALL GOES RIGHT... OR LEFT
    if ball.xcor() > 380: 
        ball.reset_position()
        scoreboard.l_score += 1
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_score += 1

#TO BE CONTINUED...






    





#=============================END================================#
screen.exitonclick()