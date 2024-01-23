from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(500, 400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

x = -230
y = 170
for n in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[n])
    new_turtle.up()
    new_turtle.goto(x, y)
    y -= 60
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. The {winning_color} turtle is the winner")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner")


        random_distance = randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
