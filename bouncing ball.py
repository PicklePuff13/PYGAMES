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
ball1=Bouncyballs(350,75,37)
ball2=Bouncyballs(450,100,55)
ball3=Bouncyballs(550,125,65)
bouncies=[ball1,ball2,ball3]
def draw():
    for ball in bouncies:
      ball.draw()
def update(t):
    pass
    #constant acceleration 
    for ball in bouncies:
      uy=ball.vy
      ball.vy+=Gravity*t
      ball.starty+=(uy+ball.vy)*0.5*t

    #detecting and handling bounce
      if ball.starty>695:
          ball.starty=695
          ball.vy=-ball.vy*0.9
      ball.startx+=ball.vx*t
    #restricting left and right edges
      if ball.startx>695 or ball.startx<55:
          ball.vx=-ball.vx

def on_key_down(key):
    if key==keys.SPACE:
        ball1.vy=-850
        ball2.vy=-850
        ball3.vy=-850

pgzrun.go()
