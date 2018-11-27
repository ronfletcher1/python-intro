
from math import hypot
from pygame.sprite import Sprite
import pygame

class BadGuy(Sprite):
    def __init__(self):
        super(BadGuy,self).__init__()
        # x and y is where the image is drawn!
        # but they are no good for collisions.  we need rect for that
        self.x = 200
        self.y = 200
        self.speed = 4
        # rect is short for rectangle to create borders around the image so they can collide
        # capitalized because it's a class "Rect"
        self.rect = pygame.Rect(0,0,32,32)
        # moves the rectangle to where the guy is
        self.rect.centerx = self.x
        self.rect.top = self.y
    def update_me(self, theHero):
        dx = self.x - theHero.x
        dy = self.y - theHero.y
        dist = hypot(dx, dy)
        dx = dx / dist
        dy = dy /dist
        self.x -= dx * self.speed
        self.y -= dy * self.speed
        self.rect.x = self.x
        self.rect.x = self.y