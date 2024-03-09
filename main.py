import time
from turtle import Turtle, Screen
from  snake import Snake
from food import Food
from  scoreboard import ScoreBoard
score=0
s=Screen()
s.setup(600,600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)
sn=Snake()
sc=ScoreBoard()
food = Food()
s.listen()
s.onkey(sn.up, "Up")
s.onkey(sn.down, "Down")
s.onkey(sn.right, "Right")
s.onkey(sn.left, "Left")
not_over=True
while not_over:
    s.update()
    time.sleep(0.1)
    sn.move()
    if sn.head.distance(food) < 15:
        food.ref()
        sn.extend()
        sc.increase_score()

    if sn.head.xcor() > 280 or sn.head.ycor() < -280 or sn.head.xcor()< -280 or sn.head.ycor() > 280:
        sc.res()
        sn.res()


    for se in sn.seg[1:]:
        if sn.head.distance(se)<10:
            sc.res()
            sn.res()


s.exitonclick()