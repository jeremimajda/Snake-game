import turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.starting_x = 0
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for segment in range(0, 3):
            p_of_snake = turtle.Turtle("square")
            p_of_snake.penup()
            p_of_snake.color("white")
            p_of_snake.goto(self.starting_x, 0)
            self.starting_x -= 20
            self.segments.append(p_of_snake)

    def add_segment(self, position):
        p_of_snake = turtle.Turtle("square")
        p_of_snake.penup()
        p_of_snake.color("white")
        p_of_snake.goto(position)
        self.segments.append(p_of_snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

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
