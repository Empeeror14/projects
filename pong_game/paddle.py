from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,location, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.shape("square")
        self.turtlesize(4,1)
        self.color("white")
        self.penup()
        self.goto(location)
         
        
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
        
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        