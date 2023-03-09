from turtle import Turtle

# CONSTANTS
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
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
        # creating our starting snake body
        for position in START_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # moving the last segment to the second last until it's at the front
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos(position)
        self.segments.append(new_segment)

    def extend(self):
        # append a segment to the end of the snake (segments)
        self.add_segment(self.segments[-1].position())

    def up(self):
        # shouldn't be able to go up if current heading is down
        current_heading = self.head.heading()
        if current_heading != DOWN:
            self.head.setheading(UP)

    def down(self):
        # shouldn't be able to go down if current heading is up
        current_heading = self.head.heading()
        if current_heading != UP:
            self.head.setheading(DOWN)


    def left(self):
        # shouldn't be able to go left if current heading is right
        current_heading = self.head.heading()
        if current_heading != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        # shouldn't be able to go right if current heading is left
        current_heading = self.head.heading()
        if current_heading != LEFT:
            self.head.setheading(RIGHT)
