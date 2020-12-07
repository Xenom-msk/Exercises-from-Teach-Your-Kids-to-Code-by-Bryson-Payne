import pygame
pygame.init()
screen=pygame.display.set_mode([800,600])
keep_going=True
pic=pygame.image.load("3.bmp")
radius=50
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going=False
    pygame.draw.circle(screen,pic,(400,300),radius)
    pygame.display.update()
pygame.quit()
