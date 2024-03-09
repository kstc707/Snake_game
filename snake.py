from turtle import Turtle, Screen
import time
tup = [(0, 0), (-20, 0), (-40, 0)]
dis=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake():
    def __init__(self):
        self.seg=[]
        self.create_snake()
        self.head=self.seg[0]

    def create_snake(self):
        for position in tup:
            self.add_segment(position)
    def add_segment(self,position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.seg.append(t)

    def res(self):
        for i in self.seg:
            i.goto(1000,1000)
        self.seg.clear()
        self.create_snake()
        self.head = self.seg[0]

    def extend(self):
        self.add_segment(self.seg[-1].position())

    def move(self):
        for j in range(len(self.seg) - 1, 0, -1):
            n_x = self.seg[j - 1].xcor()
            n_y = self.seg[j - 1].ycor()
            self.seg[j].goto(n_x, n_y)
        self.seg[0].forward(dis)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

