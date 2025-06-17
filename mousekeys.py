import pygame

pygame.init()
screen=pygame.display.set_mode((750,750))
c1=(153,242,82)
c2=(154,214,217)
c3=(85,127,84)
c4=(75,24,89)
c5=(24,36,89)
c6=(90,168,164)
screen.fill(c5)

pygame.display.update()

run=True

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

pygame.quit()