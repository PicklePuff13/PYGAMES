import pygame, time

pygame.init()

#defining a screen size
Screen=pygame.display.set_mode((1000,700))

#setting screen title
pygame.display.set_caption("Happy Halloween!")

#loading font
Ffont=pygame.font.SysFont('Creepfest',53)

#loading in images
Startpg=pygame.image.load('ghostpumpkin.jpg')
WLoop=True
while WLoop:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            WLoop=False
    
    #positioning the image
    Screen.blit(Startpg,(0,0))
    Text=Ffont.render('Have a happy halloween!',True,'white')
    Screen.blit(Text,(75,50))
    pygame.display.update()
     
pygame.quit()
