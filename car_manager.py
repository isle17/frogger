from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 1
STARTING_COORDINATES = [(-50, -100), (10, 140), (20, 41), (15, 181), (-20, 200), (-15, 241)]
DIRECTION_CHANGE = [0, 180, 0, 180, 0, 180, 0, 180, 0, 180]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.starting_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()
        self.cars = []
        self.create_car()

    # Created one car now we need to make 10? more
    def create_car(self):
        for x in range(0, len(STARTING_COORDINATES)):
            car = Turtle()
            car.shape("square")
            car.turtlesize(stretch_len=3.5)
            car.penup()
            car.color(COLORS[random.randint(0, len(COLORS)) - 1])
            car.goto(STARTING_COORDINATES[x])
            car.setheading(DIRECTION_CHANGE[random.randint(0, 1)])
            self.cars.append(car)

    # We made the function to create one car!
    # def create_car(self):
    #     self.shape("square")
    #     self.shapesize(stretch_len=3.5)
    #     self.penup()
    #     self.color(COLORS[random.randint(0, len(COLORS)) - 1])
    #     self.goto(STARTING_COORDINATES[0])
    #     self.setheading(180)

    # TODO Make cars movement more random
    def move(self):
        # check to see if the car is off screen 345 makes sure that the car is off screen before turing around
        for car in self.cars:
            if car.xcor() < -345:
                car.setheading(0)
                car.color(COLORS[random.randint(0, len(COLORS)) - 1])
            if car.xcor() > 345:
                car.setheading(180)
                car.color(COLORS[random.randint(0, len(COLORS)) - 1])
            car.forward(self.starting_speed)

    def increase_speed(self):
        self.starting_speed += MOVE_INCREMENT

    pass
