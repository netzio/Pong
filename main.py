from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()

screen.listen()
screen.onkey(right_paddle.down, "Down")
screen.onkey(right_paddle.up, "Up")
screen.onkey(left_paddle.down, "s")
screen.onkey(left_paddle.up, "w")

is_running = True

while is_running:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

screen.exitonclick()


