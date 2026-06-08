from turtle import Turtle, Screen, colormode
import random

dan = Turtle()
dan.penup()
dan.ht()
colormode(255)
def random_color():
    r =random.randint(0,255)
    g =random.randint(0,255)
    b =random.randint(0,255)
    color = (r,g,b)
    return color

dan.speed("fastest")
dan.setheading(225)
dan.forward(300)
dan.setheading(0)
number_of_dot = 100

for dot_count in range(1,number_of_dot + 1):
        dan.dot(20, random_color())
        dan.forward(50)
        # dan.setheading(90)
        # dan.forward(50)
        # dan.setheading(180)
        # dan.forward(500)
        if dot_count %10 == 0:
            dan.setheading(90)
            dan.forward(50)
            dan.setheading(180)
            dan.forward(500)
            dan.setheading(0)



    













my_screen = Screen()
my_screen.exitonclick()