from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.level = 1
        self.update_scoreboard()
        
        
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"level:{self.level}", align="left", font= FONT)
        
        
        
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
        
        
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)
        
