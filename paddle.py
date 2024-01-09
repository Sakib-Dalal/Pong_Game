import turtle


class Paddle(turtle.Turtle):
    def __init__(self, x):
        super().__init__()
        self.goto(x)
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()

    def paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
