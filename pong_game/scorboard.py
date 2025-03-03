from turtle import Turtle 

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score =0
        self.right_score = 0
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"Left : {self.left_score}", align="center", font=("Courier", 18, "bold"))
        self.goto(100, 250)
        self.write(f"Right : {self.right_score}", align="center", font=("Courier", 18, "bold"))
    
    def left_point(self):
        self.left_score += 1
        self.update_score()

    def right_point(self):
        self.right_score += 1
        self.update_score()