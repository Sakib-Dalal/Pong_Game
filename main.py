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

    # Detect collision with ball and wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision of ball from paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()
        

screen.exitonclick()
