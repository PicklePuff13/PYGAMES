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

class circles():
    def __init__(self,colour,centre,radius,width=0):
        self.colour=colour
        self.centre=centre
        self.radius=radius
        self.width=width
        self.screen=screen

    def cirdraw(self):
        pygame.draw.circle(self.screen,self.colour,self.centre,self.radius,self.width)
    
    def cirgrow(self,growf):
        self.radius+=growf
        pygame.draw.circle(self.screen,self.colour,self.centre,self.radius,self.width)




#object creation
circle1=circles(c6,(325,325),97)
circle2=circles(c2,(325,325),77)
circle3=circles(c1,(325,325),67)
circle4=circles(c4,(325,325),57)

run=True

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            circle1.cirdraw()
            circle2.cirdraw()
            circle3.cirdraw()
            circle4.cirdraw()
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            circle1.cirgrow(10)
            circle2.cirgrow(10)
            circle3.cirgrow(10)
            circle4.cirgrow(10)
            pygame.display.update()
        elif event.type==pygame.MOUSEMOTION:
            mousecord=pygame.mouse.get_pos()
            circlen=circles(c3,(mousecord),9)
            circlen.cirdraw()
            pygame.display.update()
            

        

pygame.quit()
