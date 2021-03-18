from turtle import Turtle, Screen
from random import randint,random
#=============SCREEN=================#
screen = Screen()
screen.setup(width=500,height=400)
#===================VARIABLES=========================#
user_bet = screen.textinput(title="make your bet: ", prompt="Which turtle will win? ")
colors=['red','green','yellow','blue','purple','orange']
color_idx = 0
x=-230
y=150
is_race_on = False
all_turtles = []
#=========================================================#
#Generate new turtles
for _ in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x,y)
    new_turtle.color(colors[color_idx])
    y-=50
    color_idx+=1
    all_turtles.append(new_turtle)
#==============================START===================================#
if user_bet: #Game doesnt start until user enters bet
    is_race_on = True
while is_race_on: #as long as race still on...
    for turtle in all_turtles: #for each turtle in above list...
        if turtle.xcor() > 230: #if reaches end of screen...
            is_race_on = False #end race...
            winning_color = turtle.pencolor() #identify winning color
            if winning_color == user_bet: #if winner same as user bet...
                print(f"Your {winning_color} turtle won!!!")
            else: #else...
                print(f"Sorry, your {user_bet} did not win... :(")
        #Keep nudging turtles forward!
        rand_distance = randint(0,10)
        turtle.forward(rand_distance)
#===============================END=====================================#
screen.exitonclick()