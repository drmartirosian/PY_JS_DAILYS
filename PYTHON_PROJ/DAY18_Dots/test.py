
#===================================18======================================#
# from turtle import * #IMPORT EVERYTHING
from turtle import Turtle,Screen
from random import randint




#==============================START====================================#
timmy = Turtle() #Generate turtle object "timmy"

# timmy.shape("turtle")
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

# for j in range(len(angles)+1):
#     for i in range(num_turns):
#         print(i)
#         timmy.left(angles[current_angle_len])
#         timmy.forward(100)
#     num_turns += 1
#     current_angle_len+=1



#----------------------RANDOM PATH GENERATOR----------------------------------
colors = ['red','blue','yellow','green','black','orange']
timmy.pensize(10)
timmy.speed('fastest')

def go_down():
    timmy.right(90)
    timmy.forward(50)
    timmy.left(90)
def go_up():
    timmy.left(90)
    timmy.forward(50)
    timmy.right(90)
def go_right():
    timmy.forward(50)
def go_left():
    timmy.backward(50)

for i in range(50):
    rand_num = randint(1,4)
    timmy.color(colors[randint(0,5)])

    if rand_num == 1:
        go_up()
    elif rand_num == 2:
        go_down()
    elif rand_num == 3:
        go_right()
    else:
        go_left()
#--------------------------------------------------------

#================================END=====================================#
my_screen = Screen() # Show in screen, 
my_screen.exitonclick() # exist ONLY on click

