from turtle import Screen
from random import randint, random
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600,height=600) 
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake() #generate snake
food = Food() #generate food

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


screen.exitonclick()