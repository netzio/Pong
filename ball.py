from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0, 0)
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        next_x = self.xcor() + self.x_move
        next_y = self.ycor() + self.y_move
        self.goto(next_x, next_y)
        if self.ycor() >= 280:
            self.bounce()
        elif self.ycor() <= -280:
            self.bounce()

    def bounce(self):
        self.y_move *= -1
