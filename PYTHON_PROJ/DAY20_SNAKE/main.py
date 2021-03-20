#================IMPORTS========================#
from turtle import Screen, Turtle
from random import randint, random
import time
#=====================SCREEN=====================#
screen = Screen()
screen.setup(width=600,height=600) #Screen dimensions
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0) #no animations, keep snake body together
#======================START=======================#

#GENERATE SNAKE BODIES
start_positions = [(0,0),(-20,0),(-40,0)]
segments = []#Hold snake bodies
for position in start_positions:
    new_segment = Turtle(shape="square")
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)
    
#MOVE SNAKE
game_is_on = True 
while game_is_on: 
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1,0,-1): #Move segments by rear segments taking x,y of front segments(start, stop, step)
        new_x = segments[seg_num-1].xcor() #x coord of 2nd to last
        new_y = segments[seg_num-1].ycor() #x coord of 2nd to last
        segments[seg_num].goto(new_x,new_y) #last segment
    segments[0].forward(20)











#======================START=======================#
screen.exitonclick()