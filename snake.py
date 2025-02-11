from turtle import Turtle 

STARTING_POSITIONS = [(0,0), (-20,0), (-40, 0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.addPosition(position)

    def addPosition(self, position):
            segment = Turtle("square")
            segment.color("white")    
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def extend(self):
        self.addPosition(self.segments[-1].position())


    def up(self):
        if self.head.heading() != DOWN:
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

    def isCollidingWithWall(self):
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            return True
        else:
            return False

    def move(self):
        for segment in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()

            self.segments[segment].goto(new_x, new_y)
        
        self.head.forward(MOVE_FORWARD)