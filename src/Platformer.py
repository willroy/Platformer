import pygame
import man
from pygame.locals import*

pygame.display.set_caption('JustAnotherPlatformerGame') #Sets title for window
Window = pygame.display.set_mode((800,500)) #Sets Width and height
White = (255,255,255) #Define White
Red = (255, 0, 0) #Define Red
Black = (0, 0, 0) #Define Black
Green = (0, 255, 0) #Define Green
Box1 = pygame.Rect(20, 20, 100, 100)

man = man.Goblin()

def update():
    Window.fill(Red) #Type Black, Red, Green Or White
    Window.blit(man.image, man.rect)
Box2 = pygame.Rect(150, 50, 100, 95)
Box3 = pygame.Rect(350, 350, 50, 50)
Box4 = pygame.Rect(200, 200, 150, 150)
Box5 = pygame.Rect(400, 10, 100, 125)
Line1 = pygame.draw.line(Black, 100, 200, 1)
Window.fill(White) #Type Black, Red, Green Or White
Window.fill(Red, Box1)
Window.fill(Green, Box2)
Window.fill(Green, Box3)
Window.fill(Red, Box4)
Window.fill(Black, Box5)
WIndow.fill(Line1)
    pygame.display.flip() #Updates the display on the window
print "SUCCESS"
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
#Added Boxes
