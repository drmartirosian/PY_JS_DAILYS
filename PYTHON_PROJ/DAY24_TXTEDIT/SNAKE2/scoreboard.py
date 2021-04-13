from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        #READ HIGH_SCORE FROM DATA.TXT FILE
        with open('data.txt', mode='r') as data:
            self.high_score = int(data.read())

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} || Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self): #replaces game over, resets scoreboard
        if self.score > self.high_score:
            self.high_score = self.score

            with open('data.txt',mode='w') as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
