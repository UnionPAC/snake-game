from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("SkyBlue")
        # creating food fast, so no animations
        self.speed("fastest")
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.turtlesize(0.6, 0.6, 0)
        self.set_food()

    def set_food(self):
        # need to spawn food at random location
        # the size of our grid is: 600 x 600
        # so we need a random x & y between 0 and 600
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.setpos(x=rand_x, y=rand_y)
