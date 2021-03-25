from turtle import Screen
from random import randint, random
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600) 
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake() #generate snake
food = Food() #generate food
scoreboard = Scoreboard() #scoreboard

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
    #check distance of snake head to food, less than 15, then they collided
    if snake.head.distance(food) < 15: # distance() returns distance between 2 things
        food.refresh() #if food eaten, make new food
        snake.extend()
        scoreboard.increase_score()

    #DETECT WALL COLLISIONS
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    
    #DETECT TAIL COLLISIONS
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    #if head colides with any segment in tail...
        #trigger game over
    



screen.exitonclick()