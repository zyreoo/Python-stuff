from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_SPEED = 0.1

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        color_number = random.randint(0, len(COLORS) - 1)
        self.color(COLORS[color_number])
        y = random.randint(0,230)
        self.goto(250, y)
        self.speed(STARTING_SPEED)
        self.setheading(180)
    
    def move(self):
        self.fd(STARTING_MOVE_DISTANCE)

    def move_increament(self):
        self.speed(STARTING_SPEED * MOVE_INCREMENT)

    
