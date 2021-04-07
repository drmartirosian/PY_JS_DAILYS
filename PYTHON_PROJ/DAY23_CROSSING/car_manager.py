
from turtle import Turtle
from random import randint, random
from player import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1,6) #TOO MANY CARS< THIS MAKES FEWER
        if random_chance == 1:
            new_car = Turtle('square')
            # new_car.shape('square')
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.color(COLORS[randint(0,5)])
            # new_car.setheading(180)
            random_y = randint(-250,250)
            new_car.goto(320,random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT
