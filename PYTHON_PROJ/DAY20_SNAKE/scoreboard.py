from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier",12,"normal")



class Scoreboard(Turtle): #now Scoreboard class can do everything Turtle class can

    def __init__(self):
        super().__init__() #initialize inherited class (Turtle)
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0,250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"SCORE: {self.score}", align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1 #increase score by 1
        self.clear() #clear prior scoreboard
        self.update_scoreboard() #show increased score

