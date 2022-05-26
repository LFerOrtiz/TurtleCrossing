from turtle import Turtle

ALIGNMENT = "center"
NORMAL_FONT = ("Bauhaus 93", 16, "normal")
BIG_FONT = ("Bauhaus 93", 22, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.update()

    def update(self):
        """ Update the score in the scoreboard """
        self.clear()
        self.goto(x=-250, y=270)
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=NORMAL_FONT)

    def point(self):
        """ Add a point to the scoreboard """
        self.score += 1
        self.update()

    def game_over(self):
        """ print 'game over' in the screen """
        self.update()
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=NORMAL_FONT)
