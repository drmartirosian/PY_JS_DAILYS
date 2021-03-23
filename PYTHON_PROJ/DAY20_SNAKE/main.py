from turtle import Screen, Turtle
from random import randint, random
from snake import Snake
import time

screen = Screen()
screen.setup(width=600,height=600) 
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake() #generate snake

screen.listen() #listen for keystrokes
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")

    
game_is_on = True 
while game_is_on: 
    screen.update() #refresh screen
    time.sleep(0.1) #delay 0.1 second
    snake.move()


screen.exitonclick()