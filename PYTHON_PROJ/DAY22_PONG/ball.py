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
        self.x_move = 10
        self.y_move = 10

    def move(self): #Keep moving ball
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self): #If hits cieling/floor
        self.y_move *= -1
    
    def bounce_x(self): #If hits paddles
        self.x_move *= -1
    
    def reset_position(self): #Respawn ball
        self.goto(0,0) #spawn ball back at center of screen
        self.bounce_x() #after each go, reverse direction