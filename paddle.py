from turtle import Turtle


class Paddle(Turtle):
    paddle = Turtle()

    def __init__(self, pad_x, pad_y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.pad_x = pad_x
        self.pad_y = pad_y
        self.goto(pad_x, pad_y)

    def up(self):
        paddle_y = self.ycor() + 20
        self.goto(self.pad_x, paddle_y)

    def down(self):
        paddle_y = self.ycor() - 20
        self.goto(self.pad_x, paddle_y)
