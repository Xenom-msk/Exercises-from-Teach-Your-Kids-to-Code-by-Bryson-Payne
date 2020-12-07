import pygame
pygame.init()
screen=pygame.display.set_mode([800,600])
keep_going=True
pygame.display.set_caption("Click to draw")
TURQUOISE=(50,255,255)
radius=15

while keep_going:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            keep_going=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            spot=event.pos
            pygame.draw.circle(screen,TURQUOISE,spot,radius)
            pygame.display.update()
pygame.quit()
    
