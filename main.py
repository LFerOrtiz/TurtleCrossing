from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
import time

game_on = True

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = ScoreBoard()
car_manager = CarManager()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")

while game_on:
    screen.update()
    time.sleep(0.1)

    # Move the car along the screen
    car_manager.move()
    car_manager.return_home()

    # Check if a car hit the player
    for car in car_manager.cars:
        if 20 <= car.distance(player) < 25 or player.xcor():
            print(car.distance(player))
            game_on = False
            score.game_over()

    # Return the player if the player is on finish line
    if player.finish_line():
        score.point()
        car_manager.speed_up()

screen.exitonclick()
