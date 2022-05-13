from random import random
from turtle import Turtle, Screen, clear
import random

is_race_on = False
all_turtles = []

screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput('신나는 거북이 게임!','거북이를 선택하세요' )

y_position = [-70, -40, -10, 20, 50, 80]
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'black']

for turtle_index in range(6):
    one = Turtle(shape='turtle')
    one.color(colors[turtle_index])
    one.penup()
    one.goto(x=-230,y=y_position[turtle_index])
    all_turtles.append(one)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("User Win~!")
            else:
                print(f'You lose! {winning_color} wins!')
            break
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        

screen.exitonclick()

