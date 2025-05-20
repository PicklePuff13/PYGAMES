import pygame

#initialising pygame
pygame.init()
blobscreen=pygame.display.set_mode((750,750))
blobscreen.fill("light green")
pygame.display.update()

class rectangles():
    def __init__(self, dimensions, colour):
        self.screen=blobscreen
        self.colour=colour
        self.dimensions=dimensions
    def recdraw(self):
        self.drawrect=pygame.draw.rect(self.screen,self.colour,self.dimensions)
#object creation
blob=rectangles((100,100,50,75),"black")
blob2=rectangles((600,100,50,75),"black")
blob3=rectangles((175,140,400,50),"black")

Pickle=True
while Pickle:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Pickle=False
    blob.recdraw()
    blob2.recdraw()
    blob3.recdraw()
    pygame.display.update()

    

