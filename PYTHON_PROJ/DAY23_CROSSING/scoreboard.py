FONT = ("Courier", 14, "normal")
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.level = 1

        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"LEVEL: {self.level}",font=FONT, align='left')

    def increment_level(self):
        self.level += 1
        self.update_scoreboard()
    
    def reset_score(self):
        self.level = 1
        self.update_scoreboard()




