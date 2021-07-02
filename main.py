import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# TODO somewhere in here i want to add some power ups, unleash the turtlezilla!


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# draw_circle = Turtle()
# draw_circle.penup()
# draw_circle.goto(-50, -140)
# draw_circle.pendown()
# draw_circle.circle(40)
# draw_circle.penup()
# draw_circle.goto(x=-100, y=-110)
# draw_circle.pendown()
# draw_circle.goto(x=100, y=-110)

# Create the player
player = Player()
cars = CarManager()
scoreboard = Scoreboard()
# Get the screen to listen
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
screen.onkey(player.move_down, "Down")

game_is_on = True
while game_is_on:
    cars.move()
    if player.ycor() == 280:
        scoreboard.update_score()
        player.reset_player()
        cars.increase_speed()
    for car in cars.cars:
        if player.distance(car) < 42 and car.ycor() + 20 > player.ycor() > car.ycor() - 30:
            game_is_on = False
    time.sleep(0.01)
    screen.update()


screen.exitonclick()
