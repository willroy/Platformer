import pygame 
from pygame.locals import*
pygame.display.set_caption('JustAnotherPlatformerGame') #Sets title for window
Window = pygame.display.set_mode((800,500)) #Sets Width and height
White = (255,255,255) #Define White
Red = (255, 0, 0) #Define Red
Black = (0, 0, 0) #Define Black
Green = (0, 255, 0) #Define Green
Window.fill(White) #Type Black, Red, Green Or White
running = True
pygame.display.flip() #Updates the display on the window

while running: #While loop
    event = pygame.event.wait ()
    if event.type == pygame.QUIT: #when you click [x] it quits
        running = False
pygame.quit() #quits


