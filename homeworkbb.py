from turtle import Screen
import pgzrun,random

WIDTH=750
HEIGHT=750

Red=random.randint(0,255)
Green=random.randint(0,255)
Blue=random.randint(0,255)
Colour=Red,Green,Blue
Gravity=2000.0

#class for square
class Bouncysquares ():
    def __init__(self,startx,starty):
        self.startx=startx
        self.starty=starty
        self.vx=250
    def draw(self):
        Red=random.randint(0,255)
        Green=random.randint(0,255)
        Blue=random.randint(0,255)
        Colour=Red,Green,Blue
        pos=(self.startx,self.starty)
        screen.draw.filled_rect(rect,(Colour))
#object for class
square1=Bouncysquares(350,75,37)
square2=Bouncysquares(450,100,55)
square3=Bouncysquares(550,125,65)
bouncies=[square1,square2,square3]
def draw():
    for square in bouncies:
      square.draw()
def update(t):
    pass
    #constant acceleration 
    for square in bouncies:
      uy=square.vy
      square.vy+=Gravity*t
      square.starty+=(uy+square.vy)*0.5*t

    #detecting and handling bounce
      if square.starty>695:
          square.starty=695
          square.vy=-square.vy*0.9
      square.startx+=square.vx*t
    #restricting left and right edges
      if square.startx>695 or square.startx<55:
          square.vx=-square.vx

def on_key_down(key):
    if key==keys.SPACE:
        square1.vy=-850
        square2.vy=-850
        square3.vy=-850

pgzrun.go()