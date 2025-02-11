from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,260)
        self.color("white")
        self.updateScore()
        self.hideturtle()

    def updateScore(self):
        self.clear()
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def gameOver(self):
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)
        

    def increaseScore(self):
        self.score += 1
        self.updateScore()
        