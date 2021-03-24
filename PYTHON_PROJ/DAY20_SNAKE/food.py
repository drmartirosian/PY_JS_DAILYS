from turtle import Turtle
from random import randint, random


class Food(Turtle): #inherit Turtle class functions into Food class

    def __init__(self): # Make food dot
        super().__init__() #initialize inherited class (Turtle)
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) #stretch circle
        self.color('blue')
        self.speed('fastest')
        self.refresh() #generate new food location

    def refresh(self): # Generate a new food
        random_x = randint(-280,280)
        random_y = randint(-280,280)
        self.goto(random_x,random_y)