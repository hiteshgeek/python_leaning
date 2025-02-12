from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.goto(0, 260)    
        self.clear()
        self.level += 1
        self.write(f"Level : {self.level}", align="center", font=("Courier", 18, "bold"))

    def game_over(self):
        self.goto(0, 0)    
        self.clear()
        self.write(f"Game Over", align="center", font=("Courier", 18, "bold"))

