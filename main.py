from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")


tim = Turtle()
tom = Turtle()
tim.shape('turtle')
tom.shape('turtle')
tim.color('red')
tom.color('purple')
tim.teleport(-400, 200)
tom.teleport(-400, 100)



print(user_bet)
screen.exitonclick()