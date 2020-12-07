import pygame
pygame.init()
screen=pygame.display.set_mode([800,600])
keep_going=True
pic=pygame.image.load("B).bmp")
colorkey=pic.get_at((0,0))      # ???
pic.set_colorkey(colorkey)      # ???
picx=0
picy=0
TURQUOISE=(50,255,255)
timer=pygame.time.Clock()
speedx=4
speedy=4

while keep_going:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            keep_going=False

    picx+=speedx
    picy+=speedy

    if picx<=0 or picx+pic.get_width()>=800:
        speedx=-speedx

    if picy<=0 or picy+pic.get_height()>=600:
        speedy=-speedy
        
    screen.fill(TURQUOISE)
    screen.blit(pic,(picx,picy))
    pygame.display.update()
    timer.tick(60)
pygame.quit()
