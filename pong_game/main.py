from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

main_screen = Screen()
main_screen.title("main screen")
main_screen.setup(width=800, height=600)
main_screen.bgcolor("black")
main_screen.tracer(0)

scoreboard = ScoreBoard()
ball = Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

main_screen.listen()
main_screen.onkey(r_paddle.go_up, "Up")
main_screen.onkey(r_paddle.go_down, "Down")
main_screen.onkey(l_paddle.go_up, "w")
main_screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.init_speed)
    main_screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.r_score > 5 or scoreboard.l_score > 5:
        if scoreboard.r_score > scoreboard.l_score:
            print(f"2P Win")
        else:
            print("1P Win!")

        game_is_on = False


main_screen.exitonclick()