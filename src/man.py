import pygame
import os

class Goblin(pygame.sprite.Sprite):

    def __init__(self):
        filename = os.path.realpath(__file__)
        dirname = os.path.split(filename)[0]
        self.imagepath = os.path.join(dirname, "resources", "goblin.png")
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.image = self.get_image()
        self.rect = self.image.get_rect()

    def get_image(self):
        print "Goblin: %s " % self.imagepath
        return pygame.image.load(self.imagepath).convert()

    def move_right(self):
        self.rect = self.rect.move(10, 0)
