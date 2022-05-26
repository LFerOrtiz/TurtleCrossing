from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class Car(Turtle):
    def __init__(self):
        super().__init__()
        """ Create a car along the Y axis """
        y_init = random.randrange(-230, 250, 40)
        x_init = random.randrange(-280, 320, 20)
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1.5, stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(x_init, y_init)

    def car_home(self):
        """ Return the car to home position """
        y_home = random.randrange(-235, 240, 40)
        self.goto(320, y_home)


class CarManager:
    def __init__(self):
        self.cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE
        self.create()

    def create(self):
        """ Create a list with different cars """
        for num in range(0, 20):
            new_car = Car()
            self.cars.append(new_car)

    def move(self):
        """ Move the cars across the screen """
        for car in self.cars:
            new_x = car.xcor() - self.cars_speed
            car.goto(new_x, car.ycor())

    def return_home(self):
        """ Return the car to the home position """
        for car in self.cars:
            if car.xcor() < -315:
                car.car_home()

    def speed_up(self):
        """ Speed up the cars """
        if self.cars_speed < 15:
            self.cars_speed += MOVE_INCREMENT
