from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    # TODO 1 initialize
    # TODO 2 track player level
    # TODO 3
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-270, 270)
        self.score = 0
        self.write(f"Score: {self.score}", font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", font=FONT)



