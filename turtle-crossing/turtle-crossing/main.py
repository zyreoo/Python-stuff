import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import threading
# from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()


screen.listen()
screen.onkey(player.move, "Up")

cars = []
def generate_car():
    car =  CarManager()
    cars.append(car)
    screen.ontimer(generate_car, 600)


generate_car()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    for car in cars:
        car.move()

    for car in cars:
        if player.distance(car) < 20:
            game_is_on = False

    if player.ycor() == 280:
        player.restart()
        for car in cars:
            car.move_increament()
