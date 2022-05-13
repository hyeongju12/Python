from turtle import Screen, Turtle
import turtle
import random

tim = Turtle()

tim.color('blue')
tim.shape('turtle')

screen = Screen()
screen.colormode(255)
tim.speed(10.5)

def draw_spirograph(gab):
    for _ in range(int(360/gab)):
        tim.pensize(2)
        tim.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        currnet_heading = tim.heading()
        tim.setheading(currnet_heading+gab)
        tim.circle(100)

draw_spirograph(5)

screen.mainloop()


