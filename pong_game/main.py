from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scorboard import Scoreboard

screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")

screen.tracer(0)

paddle_right = Paddle((350,0))
paddle_left = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.update()

screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

game_is_on = True

while game_is_on:    
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()  

    y_cor = ball.ycor()

    if y_cor > 280 or y_cor < -280:
            ball.bounce_y()
    
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        scoreboard.right_point()
    elif ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        scoreboard.left_point()

    if ball.xcor() > 380:
         ball.reset_ball()
        
    if ball.xcor() < -380:
         ball.reset_ball()

screen.exitonclick()