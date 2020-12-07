import pygame
import random
pygame.init()
screen=pygame.display.set_mode([200,150])

keep_going=True
timer=pygame.time.Clock()

while keep_going:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            keep_going=False
    radius=random.randint(1,60)
    RNDRGB=(random.randint(0,255),random.randint(0,255),random.randint(0,255)) 
    pygame.draw.circle(screen,RNDRGB,(100,75),radius)
    pygame.display.update()
    timer.tick(20)
    
pygame.quit()
