import turtle
from turtle import Turtle

with open("data.txt") as high:
    a=high.read()
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score = int(a)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()
    print(a)
    def update_score(self):
        self.clear()
        self.write(f"SCORE={self.score} High Score={self.high_score}", align="center",font=('Arial', 16, 'normal'))

    def res(self):
        if self.score > self.high_score:
            with open("data.txt",mode="w") as high:
                high.write(str(self.score))
            with open("data.txt") as high:
                a=high.read()
            self.high_score=int(a)
        self.score = 0
        self.update_score()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=('Arial', 16, 'normal'))

    def increase_score(self):
        self.score+=1
        self.update_score()
