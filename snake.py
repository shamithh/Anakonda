import turtle
STARTING_POSITION = [(0 , 0) , (-20 , 0), (-40 , 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.fragments = []
        self.create_snake()
        self.head = self.fragments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_fragment(position)

    def add_fragment(self , position):
        new_fragment = turtle.Turtle("square")
        new_fragment.color("white")
        new_fragment.penup()
        new_fragment.goto(position)
        self.fragments.append(new_fragment)

    def extend(self):
        self.add_fragment(self.fragments[-1].position())


    def move(self):
        for frag_num in range(len(self.fragments) - 1, 0, -1):
            new_x = self.fragments[frag_num - 1].xcor()
            new_y = self.fragments[frag_num - 1].ycor()
            self.fragments[frag_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def snake_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def snake_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)