from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0

        self.write_score()

    def write_score(self):
        self.penup()
        self.hideturtle()
        self.goto(-290,270)
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Level : {self.score+1}", align="Left", font=FONT)

    def level_up(self):
        self.score += 1
        self.refresh_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="Center", font=("Courier", 25, "normal"))
