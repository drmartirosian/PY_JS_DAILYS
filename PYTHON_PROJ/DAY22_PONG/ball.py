from turtle import Turtle


class Ball(Turtle):
    X_POS = 0
    Y_POS = 0
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(self.X_POS,self.Y_POS)
        # self.shapesize(stretch_wid=1,stretch_len=1)
    def move(self):
        new_x = self.xcor()+10
        new_y = self.ycor()+10
        self.goto(new_x,new_y)
