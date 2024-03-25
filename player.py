from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.setheading(90)

    def move_player(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def reset_loc(self):
        self.goto(STARTING_POSITION)
