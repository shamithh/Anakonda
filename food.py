import turtle
import random

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7,stretch_wid=0.7)
        self.color("silver")
        self.speed("fastest")
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x , random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


