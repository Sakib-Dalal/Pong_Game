import turtle


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(1, 1)

    def move(self):
        self.x_pos = self.xcor() + 10
        self.y_pos = self.ycor() + 10
        self.goto(self.x_pos, self.y_pos)