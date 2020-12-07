import pygame
pygame.init()
screen=pygame.display.set_mode([600,600])
keep_going=True
pic=pygame.image.load("B).bmp")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
picx=0
picy=0
BLACK=(0,0,0)
timer=pygame.time.Clock()    # Timer for animation

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going=False

    picx+=1   # Move picture on 1 pixel
    picy+=1

    screen.fill(BLACK)                # Clear screen
    screen.blit(pic,(picx,picy))
    pygame.display.update()
    timer.tick(60)                    # Limit to 60 fps
    
pygame.quit()                         # Exit
    
