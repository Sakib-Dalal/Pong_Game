import turtle

screen = turtle.Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()

turtle.tracer(0)  # no animation

y_pos = 0
paddle = turtle.Turtle()
paddle.goto(350, y_pos)
paddle.color("white")
paddle.shape("square")
paddle.shapesize(5, 1)
paddle.penup()


def paddle_up():
    global y_pos
    y_pos += 20
    paddle.goto(paddle.xcor(), y=y_pos)


def paddle_down():
    global y_pos
    y_pos -= 20
    paddle.goto(paddle.xcor(), y=y_pos)


turtle.onkey(key="Up", fun=paddle_up)
turtle.onkey(key="Down", fun=paddle_down)

is_game_on = True
while is_game_on:
    screen.update()

screen.exitonclick()
