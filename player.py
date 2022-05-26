from turtle import Turtle

INITIAL_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black", "green")
        self.setheading(90)
        self.penup()
        self.goto(INITIAL_POSITION)

    def move_up(self):
        """ Move the turtle up"""
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(x=self.xcor(), y=new_y)

    def finish_line(self):
        """ Check if the player is in the finish line"""
        if self.ycor() > FINISH_LINE_Y:
            self.goto(INITIAL_POSITION)
            return True
