import pygame
import man
from pygame.locals import*

pygame.display.set_caption('JustAnotherPlatformerGame') #Sets title for window
Window = pygame.display.set_mode((800,500)) #Sets Width and height
White = (255,255,255) #Define White
Red = (255, 0, 0) #Define Red
Black = (0, 0, 0) #Define Black
Green = (0, 255, 0) #Define Green
Window.fill(Red) #Type Black, Red, Green Or White

man = man.Goblin()

def update():
    Window.fill(Red) #Type Black, Red, Green Or White
    Window.blit(man.image, man.rect)
    pygame.display.flip() #Updates the display on the window

update()

running = True

while running: #While loop
    event = pygame.event.wait()
    if event.type == pygame.QUIT: #when you click [x] it quits
        running = False
    elif event.type == pygame.KEYDOWN:
        man.move_right()
        update()
    else:
        print "Event Type: %s" % event.type

pygame.quit() #quits

# Updated by ant.

