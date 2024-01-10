import turtle


class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align="center", font=('Courier', 30, 'normal'))
        self.goto(100, 250)
        self.write(self.r_score, align="center", font=('Courier', 30, 'normal'))

    def score_r_paddle(self):
        self.r_score += 1
        self.print_score()

    def score_l_paddle(self):
        self.l_score += 1
        self.print_score()
