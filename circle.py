import pygame

#initialising pygame
pygame.init()
blobscreen=pygame.display.set_mode((750,750))
blobscreen.fill("light green")
pygame.display.update()

class circles():
    def __init__(self, center, radius, color):
        self.screen=blobscreen
        self.surface=blobscreen
        self.center=center
        self.radius=radius
        self.colour=color
    def cirdraw(self):
        self.drawcircle=pygame.draw.circle(self.surface, self.colour, self.center, self.radius)
#object creation
blob=circles((325,325),55,"black")
blob2=circles((125,125),65,"black")
blob3=circles((525,525),45,"black")

Pickle=True
while Pickle:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Pickle=False
    blob.cirdraw()
    blob2.cirdraw()
    blob3.cirdraw()
    pygame.display.update()
