from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0 
        self.update()
        
        
    def update(self):
        self.goto(-100, 200)
        self.write(self.l_score,align="center", font=("Arail", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score,align="center", font=("Arail", 60, "normal"))
        
        
        
    def point_to_left(self):
        self.l_score += 1
        self.clear()
        self.update()
        
        
        
    def point_to_right(self):
        self.r_score += 1
        self.clear()
        self.update()