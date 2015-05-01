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

    def move(self, x, y):
        self.rect = self.rect.move(x, y)

    def move_right(self):
        self.move(10, 0)

    def move_left(self):
        self.move(-10, 0)

    def move_up(self):
        self.move(0, -10)

    def move_down(self):
        self.move(0, 10)

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_RIGHT]:
                self.move_right()
            elif key[pygame.K_LEFT]:
                self.move_left()
            elif key[pygame.K_UP]:
                self.move_up()
            elif key[pygame.K_DOWN]:
                self.move_down()

