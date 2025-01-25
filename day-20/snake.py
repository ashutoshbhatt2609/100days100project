from turtle import Turtle
import time
START_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
DELAY=0.05

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
        self.move()


    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)
    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.pu()

        new_segment.setposition(position)
        self.segments.append(new_segment)

    def extend(self):
        #add a new segment
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_no in range(len(self.segments) - 1, 0, -1):
            new_x =self.segments[seg_no - 1].xcor()
            new_y =self.segments[seg_no - 1].ycor()
            self.segments[seg_no].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        time.sleep(DELAY)
    def up(self):
        if self.head.heading()==DOWN:
            pass
        else:
            self.head.setheading(UP)



    def down(self):
        if self.head.heading() == UP:
            pass
        else:
            self.head.setheading(DOWN)


    def right(self):
        if self.head.heading() ==LEFT:
            pass
        else:
            self.head.setheading(RIGHT)


    def left(self):
        if self.head.heading() == RIGHT:
            pass
        else:
            self.head.setheading(LEFT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]

