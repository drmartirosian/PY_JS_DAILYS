from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)] #(x,y)


class Snake():

    def __init__(self): #What to do when this class boots up
        self.segments = []#Hold snake bodies
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS: #make new segment
            new_segment = Turtle(shape="square")
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment) #add new segment
    
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1): #Move segments by rear segments taking x,y of front segments(start, stop, step)
            new_x = self.segments[seg_num-1].xcor() #x coord of 2nd to last
            new_y = self.segments[seg_num-1].ycor() #y coord of 2nd to last
            self.segments[seg_num].goto(new_x,new_y) #last segment
        self.segments[0].forward(20)