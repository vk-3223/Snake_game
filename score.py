from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,225)
        self.write(f"Score:{self.score}",align="center",font=("Arial",16,"normal"))
        self.hideturtle()
    def game_over(self):
            self.goto(0,0)
            self.write("Game is over ",align="center",font=("Arial",16,"normal"))  
            
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score:{self.score}",align="center",font=("Arial",16,"normal"))