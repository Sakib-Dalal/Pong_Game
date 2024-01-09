import turtle
import paddle
import ball
import time

screen = turtle.Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()

turtle.tracer(0)  # no animation

r_paddle = paddle.Paddle((350, 0))
l_paddle = paddle.Paddle((-350, 0))
ball = ball.Ball()

turtle.onkey(key="Up", fun=r_paddle.paddle_up)
turtle.onkey(key="Down", fun=r_paddle.paddle_down)

turtle.onkey(key="w", fun=l_paddle.paddle_up)
turtle.onkey(key="s", fun=l_paddle.paddle_down)

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    ball.move()
    screen.update()

screen.exitonclick()
