from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)] #(x,y)
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self): #What to do when this class boots up
        self.segments = []#Hold snake bodies
        self.create_snake()
        self.head = self.segments[0]

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
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN: #IF statement prevents snake from going back on self
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
