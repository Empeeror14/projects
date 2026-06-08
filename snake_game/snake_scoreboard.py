from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.color("white")
        self.write(f"Score = {self.score}", align="center", font=("Arail",20,"normal"))
        
        
        
        
        
    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align="center", font=("Arail",20,"normal"))
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!!!", align="center", font=("Arail",20,"normal"))
        