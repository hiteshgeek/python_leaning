from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Guess the winner", prompt="Which color turtle will win? : ")

colors = ["red", "green", "blue", "orange", "purple", "brown"]
is_race_on = True

turtles = []
end_height = -70
for i in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.goto(-230, end_height)
    end_height += 40

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won.")
            else:
                print(f"You lost.")
            print(f"Turtle {winning_color} won the race")
        distance = random.randint(0,10)
        turtle.forward(distance)

screen.exitonclick()