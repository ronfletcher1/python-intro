from math import hypot
from pygame.sprite import Sprite
import pygame
class the_claw(Sprite):
    def __init__(self):
        super(the_claw,self).__init__()
        self.x = 200
        self.y = 200
        self.speed = 4
        self.rect = pygame.Rect(0,0,64,64)
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