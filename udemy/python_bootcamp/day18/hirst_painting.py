import colorgram
import random
import turtle as t
color_list = [(251, 249, 245), (251, 240, 246), (234, 247, 236), (201, 167, 134), (236, 243, 249), (144, 51, 99), (163, 167, 41), (238, 71, 125), (237, 83, 
61), (17, 140, 64), (241, 221, 67), (225, 118, 163), (10, 142, 179), (67, 198, 219), (157, 59, 53), (23, 169, 129), (32, 187, 202), (127, 188, 
163), (107, 42, 88), (248, 231, 0), (236, 163, 188), (244, 168, 155), (141, 214, 224), (145, 218, 199), (136, 39, 34), (79, 36, 73), (3, 114, 36)]
t.colormode(255)

tim = t.Turtle()
tim.penup()
tim.setheading(255)
tim.forward(300)
tim.hideturtle()
tim.setheading(0)
tim.speed('fastest')
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)


    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
