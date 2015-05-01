import pygame
import man, level
from pygame.locals import*

pygame.display.set_caption('JustAnotherPlatformerGame') #Sets title for window
Window = pygame.display.set_mode((800,500)) #Sets Width and height

man = man.Goblin()
level = level.Level(Window, None)
level.add_sprite(man)

def update():
    level.update(event)
    pygame.display.flip()

print "SUCCESS"
update()

running = True

while running: #While loop
    event = pygame.event.wait()
    if event.type == pygame.QUIT: #when you click [x] it quits
        running = False
    else:
        print "Event Type: %s" % event.type
        update(event)

pygame.quit() #quits

# Updated by ant.
#Added Boxes
