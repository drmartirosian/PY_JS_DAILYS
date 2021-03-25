from turtle import Turtle

class Paddle(Turtle):
    Y_POS = 0
    X_POS = 350

    def __init__(self, position): #position x,y cordinates from class calls in main.py
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)