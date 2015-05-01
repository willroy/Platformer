import pygame
from colours import *

class Level(object):
    def __init__(self, window, level_name):
        self.level_name = level_name
        self.window = window
        self.obstacles = []
        self.sprites = []

    def redraw(self):
        self.load_level()
        for sprite in self.sprites:
            self.window.blit(sprite.image, sprite.rect)

    def update(self, event):
        self.redraw()
        for sprite in self.sprites:
            sprite.update(event)

    def add_sprite(self, sprite):
        self.sprites.append(sprite)

    def load_level(self):
        Box1 = pygame.Rect(20, 20, 100, 100)
        Box2 = pygame.Rect(150, 50, 100, 95)
        Box3 = pygame.Rect(350, 350, 50, 50)
        Box4 = pygame.Rect(200, 200, 150, 150)
        Box5 = pygame.Rect(400, 10, 100, 125)

        self.window.fill(White) #Type Black, Red, Green Or White
        self.window.fill(Red, Box1)
        self.window.fill(Green, Box2)
        self.window.fill(Green, Box3)
        self.window.fill(Red, Box4)
        self.window.fill(Black, Box5)

