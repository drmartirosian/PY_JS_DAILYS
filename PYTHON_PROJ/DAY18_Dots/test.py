
#===================================18======================================#
# from turtle import * #IMPORT EVERYTHING
from turtle import Turtle, Screen
from random import randint
import random
my_screen = Screen() # Show in screen, 
my_screen.colormode(255)
timmy = Turtle() #Generate turtle object "timmy"
timmy.pensize(15)
timmy.speed('fastest')
timmy.shape("turtle")

#==============================TEST====================================#

# timmy.dot(100,'blue')

# for i in range(10):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)


#-------------------SHAPES GENERATOR-------------------------------
#          3  4  5  6  7  8  9  10
# angles = [120,90,72,69,51,45,40,36]
# num_turns = 3
# current_angle_len = 0

# for j in range(8):
#     for i in range(num_turns):
#         timmy.left(angles[current_angle_len])
#         timmy.forward(100)
#     num_turns += 1
#     current_angle_len+=1



#----------------------RANDOM PATH GENERATOR----------------------------------
# colors = ['red','blue','yellow','green','black','orange']

# def go_down():
#     timmy.right(90)
#     timmy.forward(10)
#     timmy.left(90)
# def go_up():
#     timmy.left(90)
#     timmy.forward(10)
#     timmy.right(90)
# def go_right():
#     timmy.forward(10)
# def go_left():
#     timmy.backward(10)

# for i in range(500):
#     rand_num = randint(1,4)
#     timmy.color(colors[randint(0,5)])

#     if rand_num == 1:
#         go_up()
#     elif rand_num == 2:
#         go_down()
#     elif rand_num == 3:
#         go_right()
#     else:
#         go_left()

#------------------------RANDOM RBG-TUPLES--------------------------------

#OR...
# tuples
# my_tuple = (1,3,8)
# print(my_tuple[0])
# list(my_tuple) #converts to list

# def rand_color():
#     r = randint(0,255)
#     g = randint(0,255)
#     b = randint(0,255)
#     rand_rgb = (r,g,b)
#     return rand_rgb

# for _ in range(200):
#     timmy.color(rand_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice([0,90,180,270]))

# --------------------draw spiroghraph circle------------------

# def draw_spirograph(circle_size):
#     for _ in range(int(360/circle_size)):
#         timmy.color(rand_color())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading()+circle_size)
# draw_spirograph(5)


#================================END=====================================#
my_screen.exitonclick() # exist ONLY on click

