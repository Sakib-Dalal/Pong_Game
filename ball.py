import turtle


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(1, 1)
        self.x_move = 10
        self.y_move = 10
        self.x_pos = 0
        self.y_pos = 0
        self.move_speed = 0.1

    def move(self):
        self.x_pos = self.xcor() + self.x_move
        self.y_pos = self.ycor() + self.y_move
        self.goto(self.x_pos, self.y_pos)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()