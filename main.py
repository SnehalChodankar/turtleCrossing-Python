import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
score = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(player.move_player, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

    # Detact collision with car
    for car in cars.cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # Detact collision with top wall
    if player.ycor() >= 270:
        score.level_up()
        cars.level_up()
        player.reset_loc()

screen.exitonclick()
