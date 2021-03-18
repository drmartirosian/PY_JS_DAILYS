from turtle import Turtle, Screen
from random import randint
import random
my_screen = Screen() # Show in screen, 
my_screen.colormode(255)
timmy = Turtle() #Generate turtle object "timmy"
timmy.pensize(15)
timmy.speed('fastest')
timmy.shape("turtle")
# #==============================START====================================#
def colors():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    rand_rgb = (r,g,b)
    return rand_rgb

def dot_generator():
    #SHIFT TO NEW ROW
    for _ in range(10):
        #FILL OUT ROW
        for _ in range(10):
            timmy.color(colors())
            timmy.pendown()
            timmy.circle(5)
            timmy.penup()
            timmy.forward(50)
        timmy.penup()
        timmy.right(90)
        timmy.forward(50)
        timmy.left(90)
        timmy.backward(500)
        timmy.pendown()
dot_generator()



# #================================END=====================================#
my_screen.exitonclick() # exist ONLY on click

