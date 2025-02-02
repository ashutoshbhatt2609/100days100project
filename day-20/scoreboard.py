from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier",24,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("day-20\data.txt",mode='r') as file:
            global data
            data=int(file.read())
        self.score=0
        self.high_score=data
        self.high_score=int(self.high_score)
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.write(f"Score:{self.score} High Score: {self.high_score}",align=ALIGNMENT,font=FONT)
        self.hideturtle()
    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.high_score}", align=ALIGNMENT,font=FONT)
    def reset(self):
        if int(self.score)>int(self.high_score):
            self.high_score=str(self.score)
            with open("day-20\data.txt",mode='w') as file:
                file.write(self.high_score)
        self.score=0
        self.update_score()   
    def increase_score(self):
        self.score+=1
        self.update_score()

