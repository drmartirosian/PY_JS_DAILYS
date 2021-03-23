from turtle import Turtle
start_positions = [(0,0),(-20,0),(-40,0)] #(x,y)
segments = []#Hold snake bodies


class Snake():
    global start_positions, segments
    for position in start_positions: #make new segment
        new_segment = Turtle(shape="square")
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        segments.append(new_segment) #add new segment
    
    def move(self):
        for seg_num in range(len(segments)-1,0,-1): #Move segments by rear segments taking x,y of front segments(start, stop, step)
            new_x = segments[seg_num-1].xcor() #x coord of 2nd to last
            new_y = segments[seg_num-1].ycor() #y coord of 2nd to last
            segments[seg_num].goto(new_x,new_y) #last segment
        segments[0].forward(20)