from turtle import Turtle 

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("purple")
        self.shape("circle")
        self.penup()
        self.x_change = 10
        self.y_change = 10
        self.move_speed = 0.1

    def move(self):

        cur_x = self.xcor()
        cur_y = self.ycor()

        new_x = cur_x + self.x_change
        new_y = cur_y + self.y_change
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_change *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        self.y_change *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()    