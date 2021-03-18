from turtle import Turtle,Screen
from random import randint,random 
timmy = Turtle()
timmy.shape("turtle")
screen = Screen()
screen.listen() #START LISTENING...
#===============================START===================================#
def move_right():
    timmy.setheading(0)
    timmy.forward(10)
def move_left():
    timmy.setheading(180)
    timmy.forward(10)
def move_up():
    timmy.setheading(90)
    timmy.forward(10)
def move_down():
    timmy.setheading(270)
    timmy.forward(10)
def clear_screen():
    timmy.clear()


#Note: no () on func, otherwise would trigger right there in onkey
screen.onkey(key="w", fun=move_up) #EVENT LISTENER(listen for, do this)
screen.onkey(key="s", fun=move_down) 
screen.onkey(key="d", fun=move_right) 
screen.onkey(key="a", fun=move_left) 
screen.onkey(key="x", fun=clear_screen) 






#===============================END===================================#
screen.exitonclick()