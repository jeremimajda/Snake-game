from turtle import Turtle
from random import randint, choice

colors_of_food = ["red"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(0.7, 0.7)
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.setheading(randint(0, 360))
        self.color(choice(colors_of_food))
        self.goto(random_x, random_y)
