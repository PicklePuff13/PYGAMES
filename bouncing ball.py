import pgzrun,random

WIDTH=750
HEIGHT=750

Red=random.randint(0,255)
Green=random.randint(0,255)
Blue=random.randint(0,255)
Colour=Red,Green,Blue
Gravity=2000.0

#class for circle
class Bouncyballs ():
    def __init__(self,startx,starty,radius):
        self.startx=startx
        self.starty=starty
        self.vx=250
        self.vy=0
        self.radius=radius
    def draw(self):
        Red=random.randint(0,255)
        Green=random.randint(0,255)
        Blue=random.randint(0,255)
        Colour=Red,Green,Blue
        pos=(self.startx,self.starty)
        screen.draw.filled_circle(pos,self.radius, Colour)
#object for class
ball=Bouncyballs(450,100,55)
def draw():
    ball.draw()
def update(t):
    pass
    #constant acceleration 
    uy=ball.vy
    ball.vy+=Gravity*t
    ball.starty+=(uy+ball.vy)*0.5*t

pgzrun.go()