import pygame

class Hero(object):
    # classes always contain 2 parts
    # 1. the __init__ = runs only once
    #
    # 2. the methods = run whenever you call them
    def __init__(self):
        self.x = 100
        self.y = 100
        self.speed = 10
        self.should_move_right = False
        self.should_move_left = False
        self.should_move_down = False
        self.should_move_up = False
    def should_move(self, direction, start = True):
        if direction == "right":
            self.should_move_right = start
        if direction == "left":
            self.should_move_left = start
        if direction == "down":
            self.should_move_down = start
        if direction == "Up":
            self.should_move_up = start
    def draw_me(self):
        if(self.should_move_right):
            self.x += self.speed
        if(self.should_move_left):
            self.x -= self.speed
        if(self.should_move_down):
            self.x += self.speed
        if(self.should_move_up):
            self.x -= self.speed
