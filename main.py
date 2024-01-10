import turtle
import paddle
import ball
import time
import score

screen = turtle.Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()

turtle.tracer(0)  # no animation

r_paddle = paddle.Paddle((350, 0))
l_paddle = paddle.Paddle((-350, 0))
ball = ball.Ball()
score = score.Score()

turtle.onkeypress(key="Up", fun=r_paddle.paddle_up)
turtle.onkeypress(key="Down", fun=r_paddle.paddle_down)

turtle.onkeypress(key="w", fun=l_paddle.paddle_up)
turtle.onkeypress(key="s", fun=l_paddle.paddle_down)

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect collision with ball and wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision of ball from paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.score_l_paddle()

    if ball.xcor() < -380:
        ball.reset_position()
        score.score_r_paddle()

screen.exitonclick()
