import pygame, sys
from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode((1024,1024))
screen.fill((255,255,255))
striker = pygame.Rect(0,0,20,20)
clock = pygame.time.Clock()
x1=100
y1=150
x2=200
y2=350
if(x1>x2):
    temp=x1
    x1=x2
    x2=temp
    temp=y1
    y1=y2
    y2=temp

striker.x=x1
striker.y=y1
dy=y2-y1
dx=x2-x1
m = dy/dx
if (m<1):
    b=(2*dy)
    a=(b-(2*dx))
    p0=(b-dx)
    for k in range(0,dx):
        if (p0<0):
            striker.x=img_rect.x+5
            p0=p0+b
            all_sprites_list.draw(DISPLAYSURF)
            pygame.display.update()
            clock.tick(20)
            pygame.display.flip()
        else:
            striker.x=striker.x+5
            striker.y=striker.y+5
            p0=p0+a
            all_sprites_list.draw(DISPLAYSURF)
            pygame.display.update()
            clock.tick(20)
            pygame.display.flip()
            
        
else:
    b=(2*dx)
    a=(b-(2*dy))
    p0=((2*dx)-dy)
    for k in range(0,dy):
        if(p0<0):
            striker.y=striker.y+5
            p0=p0+(2*dx)
        else:
            striker.x=striker.x+5
            striker.y=striker.y+5
            p0=p0+a
        pygame.draw.circle(screen,(255,248,10),(striker.left + 10, striker.top + 10),10)
        clock.tick(10)
        pygame.display.update()
        pygame.display.flip()
