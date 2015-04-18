import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 500),0,32)
pygame.display.set_caption('Carrom!')
clock = pygame.time.Clock()
BLACK = (  0,   0,   0)
LIGHTBROWN = ( 255, 255, 153)
WHITE = (255, 255, 255)
BROWN = (102,51,0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0) 
BLUE  = (  0,   0, 255)

class coin(pygame.sprite.Sprite):
    def __init__(self,flag):
        pygame.sprite.Sprite.__init__(self)
        if flag==1:
            self.image=pygame.image.load("striker.png")
        elif flag==2:
            self.image=pygame.image.load("queen.png")
        elif flag==3:
            self.image=pygame.image.load("wcoin.png")
        elif flag==4:
            self.image=pygame.image.load("bcoin.png")
        elif flag==5:
            self.image=pygame.image.load("center.png")
        self.rect = self.image.get_rect()  
        self.image.set_colorkey(WHITE)
         
def skeleton():
    pygame.draw.polygon(DISPLAYSURF, LIGHTBROWN, ((50,50),(50,400),(400,400),(400,50))) 
    pygame.draw.rect(DISPLAYSURF, BLACK,(116,95,220,12),1)
    pygame.draw.rect(DISPLAYSURF, BLACK,(95,117,12,220),1)
    pygame.draw.rect(DISPLAYSURF, BLACK,(116,345,220,12),1)
    pygame.draw.rect(DISPLAYSURF, BLACK,(345,117,12,220),1)
    pygame.draw.line(DISPLAYSURF, BLACK,(82,82),(172,172))
    pygame.draw.line(DISPLAYSURF, BLACK,(82,368),(172,278))
    pygame.draw.line(DISPLAYSURF, BLACK,(368,82),(278,172))
    pygame.draw.line(DISPLAYSURF, BLACK,(278,278),(368,368))
    pygame.draw.circle(DISPLAYSURF, BLACK,(60,60),14)
    pygame.draw.circle(DISPLAYSURF, BLACK,(389,60),14)
    pygame.draw.circle(DISPLAYSURF, BLACK,(389,389),14)
    pygame.draw.circle(DISPLAYSURF, BLACK,(60,389),14)
    pygame.draw.rect(DISPLAYSURF, BROWN,(42,42,350,12))
    pygame.draw.rect(DISPLAYSURF, BROWN,(42,392,362,12))
    pygame.draw.rect(DISPLAYSURF, BROWN,(42,42,12,350))
    pygame.draw.rect(DISPLAYSURF, BROWN,(392,42,12,350))
    return
def handlecollision():
    c=1
    for i in all_sprites_list:
        if striker.rect.colliderect(i):
            dx=i.rect.x-striker.rect.x
            dy=i.rect.y-striker.rect.y
            if dx==0:
                dx=0.1
            m=(dy)/(dx) 
            ctr=0
            if abs(m)<=1:
                b=(2*abs(dy))
                a=(b-(2*abs(dx)))
                p0=(b-abs(dx))
                if m>0:
                    tempx=30
                else:
                    tempx=-30
                while (ctr*30)<=abs(dx):
                    if (p0<0):
                        i.rect.x=i.rect.x-tempx
                        p0=p0+b
                        coincollision(i,c)
                        striker_list.draw(DISPLAYSURF)
                        all_sprites_list.draw(DISPLAYSURF)
                        pygame.display.update()
                        clock.tick(40)
                        DISPLAYSURF.fill(WHITE)
                        skeleton()
                        ctr=ctr+1
                        pygame.display.flip()
                    else:
                        i.rect.x=i.rect.x-tempx
                        i.rect.y=i.rect.y-30
                        p0=p0+a
                        coincollision(i,c)
                        striker_list.draw(DISPLAYSURF)
                        all_sprites_list.draw(DISPLAYSURF)
                        pygame.display.update()
                        clock.tick(40)
                        DISPLAYSURF.fill(WHITE)
                        skeleton()
                        pygame.display.flip()
                        ctr=ctr+1
            else:
                b=(2*abs(dx))
                a=(b-(2*abs(dy)))
                p0=((2*abs(dx))-abs(dy))
                if m>0:
                    tempx=15
                else:
                    tempx=-15
                while (ctr*15)<=abs(dy):
                    if (p0<0):
                        i.rect.y=i.rect.y-15
                        p0=p0+b
                        coincollision(i,c)
                        striker_list.draw(DISPLAYSURF)
                        all_sprites_list.draw(DISPLAYSURF)
                        pygame.display.update()
                        clock.tick(40)
                        DISPLAYSURF.fill(WHITE)
                        skeleton()
                        ctr=ctr+1
                        pygame.display.flip()
                    else:
                        i.rect.x=i.rect.x-tempx
                        i.rect.y=i.rect.y-15
                        pygame.display.update()
                        p0=p0+a
                        coincollision(i,c)
                        striker_list.draw(DISPLAYSURF)
                        all_sprites_list.draw(DISPLAYSURF)
                        pygame.display.update()
                        clock.tick(40)
                        DISPLAYSURF.fill(WHITE)
                        skeleton()
                        ctr=ctr+1
                        pygame.display.flip()
    return

def coincollision(i,c):
    coinpocket()
    c=c+1
    if c<7:
        for j in all_sprites_list:
            if i.rect.colliderect(j) and i!=j:#collisions among the coins
                dx=j.rect.x-i.rect.x
                dy=j.rect.y-i.rect.y
                if dx==0:
                    dx=0.1
                m=(dy)/(dx) 
                ctr=0
                if abs(m)<=1:
                    b=(2*abs(dy))
                    a=(b-(2*abs(dx)))
                    p0=(b-abs(dx))
                    if m>0:
                        tempx=15
                    else:
                        tempx=-15
                    while (ctr*15)<=abs(dx):
                        if (p0<0):
                            j.rect.x=j.rect.x-tempx
                            p0=p0+b
                            coincollision(j,c)
                            striker_list.draw(DISPLAYSURF)
                            all_sprites_list.draw(DISPLAYSURF)
                            pygame.display.update()
                            clock.tick(40)
                            DISPLAYSURF.fill(WHITE)
                            skeleton()
                            ctr=ctr+1
                            pygame.display.flip()
                        else:
                            j.rect.x=j.rect.x-tempx
                            j.rect.y=j.rect.y-15
                            p0=p0+a
                            coincollision(j,c)
                            striker_list.draw(DISPLAYSURF)
                            all_sprites_list.draw(DISPLAYSURF)
                            pygame.display.update()
                            clock.tick(40)
                            DISPLAYSURF.fill(WHITE)
                            skeleton()
                            pygame.display.flip()
                            ctr=ctr+1
                else:
                    b=(2*abs(dx))
                    a=(b-(2*abs(dy)))
                    p0=((2*abs(dx))-abs(dy))
                    if m>0:
                        tempx=15
                    else:
                        tempx=-15
                    while (ctr*15)<=abs(dy):
                        if (p0<0):
                            j.rect.y=j.rect.y-15
                            p0=p0+b
                            coincollision(j,c)
                            striker_list.draw(DISPLAYSURF)
                            all_sprites_list.draw(DISPLAYSURF)
                            pygame.display.update()
                            clock.tick(40)
                            DISPLAYSURF.fill(WHITE)
                            skeleton()
                            ctr=ctr+1
                            pygame.display.flip()
                        else:
                            j.rect.x=j.rect.x-tempx
                            j.rect.y=j.rect.y-15
                            pygame.display.update()
                            p0=p0+a
                            coincollision(j,c)
                            striker_list.draw(DISPLAYSURF)
                            all_sprites_list.draw(DISPLAYSURF)
                            pygame.display.update()
                            clock.tick(40)
                            DISPLAYSURF.fill(WHITE)
                            skeleton()
                            ctr=ctr+1
                            pygame.display.flip()
            
    return

def coinpocket():
    for i in all_sprites_list:
        if (i.rect.x==60 and i.rect.y==60) or (i.rect.x==389 and i.rect.y==60) or (i.rect.x==60 and i.rect.y==389) or (i.rect.x==389 and i.rect.y==389):
            kill(i)

    if (striker.rect.x==60 and striker.rect.y==60) or (striker.rect.x==389 and striker.rect.y==60) or (striker.rect.x==60 and striker.rect.y==389) or (striker.rect.x==389 and striker.rect.y==389):
        kill(striker)
        
    if event.type==pygame.MOUSEBUTTONDOWN:
        if event.button==3:
            posi=pygame.mouse.get_pos()
            if posi[0]>116 and posi[0]<336 and posi[1]>345 and posi[1]<357:
                striker.rect.x=pos[0]
                striker.rect.y=345
                striker_list.draw(DISPLAYSURF)
                all_sprites_list.draw(DISPLAYSURF)
        elif event.button==1:
            linedrawing(pos)
    return
     
def linedrawing(pos):
    cor=pygame.mouse.get_pos()
    x=cor[0]
    y=cor[1]
    striker.rect.x=pos[0]
    striker.rect.y=pos[1]
    dy=(y-striker.rect.y)
    dx=(x-striker.rect.x)
    if dx==0:
        dx=0.1
    m =(dy/dx)
    tempx=0
    tempy=0
    ctr=0
    if abs(m)<1:
        b=(2*abs(dy))
        a=(b-(2*abs(dx)))
        p0=(b-abs(dx))
        if m>0:
            tempx=15
        else:
            tempx=-15
        while (ctr*30)<=abs(dx):
            if (p0<0):
                striker.rect.x=striker.rect.x-tempx
                p0=p0+b
                handlecollision()
                striker_list.draw(DISPLAYSURF)
                all_sprites_list.draw(DISPLAYSURF)
                pygame.display.update()
                clock.tick(40)
                DISPLAYSURF.fill(WHITE)
                skeleton()
                pygame.display.flip()
                ctr=ctr+1
            else:
                striker.rect.x=striker.rect.x-tempx
                striker.rect.y=striker.rect.y-15
                p0=p0+a
                handlecollision()
                striker_list.draw(DISPLAYSURF)
                all_sprites_list.draw(DISPLAYSURF)
                pygame.display.update()
                clock.tick(40)
                DISPLAYSURF.fill(WHITE)
                skeleton()
                pygame.display.flip()
                ctr=ctr+1
    else:
        b=(2*abs(dx))
        a=(b-(2*abs(dy)))
        p0=((2*abs(dx))-abs(dy))
        c=0
        if m>0:
            tempx=15
        else:
            tempx=-15
        while (ctr*15)<=abs(dy):
            if (p0<0):
                striker.rect.y=striker.rect.y-15
                p0=p0+b
                handlecollision()
                striker_list.draw(DISPLAYSURF)
                all_sprites_list.draw(DISPLAYSURF)
                pygame.display.update()
                clock.tick(40)
                DISPLAYSURF.fill(WHITE)
                skeleton()
                pygame.display.flip()
                ctr=ctr+1
            else:
                striker.rect.x=striker.rect.x-tempx
                striker.rect.y=striker.rect.y-15
                pygame.display.update()
                p0=p0+a
                handlecollision()
                striker_list.draw(DISPLAYSURF)
                all_sprites_list.draw(DISPLAYSURF)
                pygame.display.update()
                clock.tick(40)
                DISPLAYSURF.fill(WHITE)
                skeleton()
                pygame.display.flip()
                ctr=ctr+1
    return
    

q_coin_list=pygame.sprite.Group()
striker_list=pygame.sprite.Group()
center_list=pygame.sprite.Group()
w_coin_list=pygame.sprite.Group()
b_coin_list=pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
#initializing objects and adding them to the sprites array
#Striker
striker=coin(1)
striker.rect.x=127
striker.rect.y=345
striker_list.add(striker)
#Center
center=coin(5)
center.rect.x=210
center.rect.y=210
center_list.add(center)
#Queen
q_coin=coin(2)
q_coin.rect.x=225
q_coin.rect.y=225
q_coin_list.add(q_coin)
all_sprites_list.add(q_coin)
#White coin
w_coin=coin(3)
w_coin.rect.x=225
w_coin.rect.y=235
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)
w_coin=coin(3)
w_coin.rect.x=225
w_coin.rect.y=245
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)
w_coin=coin(3)
w_coin.rect.x=225
w_coin.rect.y=205
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)
w_coin=coin(3)
w_coin.rect.x=216
w_coin.rect.y=220
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)
w_coin=coin(3)
w_coin.rect.x=207
w_coin.rect.y=215
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)
w_coin=coin(3)
w_coin.rect.x=233
w_coin.rect.y=220
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)
w_coin=coin(3)
w_coin.rect.x=242
w_coin.rect.y=215
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)
w_coin=coin(3)
w_coin.rect.x=207
w_coin.rect.y=235
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)
w_coin=coin(3)
w_coin.rect.x=242
w_coin.rect.y=235
w_coin_list.add(w_coin)
all_sprites_list.add(w_coin)

#Black coin
b_coin=coin(4)
b_coin.rect.x=225
b_coin.rect.y=215
b_coin_list.add(b_coin)
all_sprites_list.add(b_coin)
b_coin=coin(4)
b_coin.rect.x=216
b_coin.rect.y=210
b_coin_list.add(b_coin)
all_sprites_list.add(b_coin)
b_coin=coin(4)
b_coin.rect.x=216
b_coin.rect.y=230
b_coin_list.add(b_coin)
all_sprites_list.add(b_coin)
b_coin=coin(4)
b_coin.rect.x=216
b_coin.rect.y=240
b_coin_list.add(b_coin)
all_sprites_list.add(b_coin)
b_coin=coin(4)
b_coin.rect.x=233
b_coin.rect.y=210
b_coin_list.add(b_coin)
all_sprites_list.add(b_coin)
b_coin=coin(4)
b_coin.rect.x=233
b_coin.rect.y=230
b_coin_list.add(b_coin)
all_sprites_list.add(b_coin)
b_coin=coin(4)
b_coin.rect.x=233
b_coin.rect.y=240
b_coin_list.add(b_coin)
all_sprites_list.add(b_coin)
b_coin=coin(4)
b_coin.rect.x=243
b_coin.rect.y=225
b_coin_list.add(b_coin)
all_sprites_list.add(b_coin)
b_coin=coin(4)
b_coin.rect.x=207
b_coin.rect.y=225
b_coin_list.add(b_coin)
all_sprites_list.add(b_coin)

all_sprites_list.draw(DISPLAYSURF)
#DISPLAYSURF.blit(pygame.image.load("center.png"),(210,210))
ctr=0
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(WHITE)
    skeleton()
    center_list.draw(DISPLAYSURF)
    striker_list.draw(DISPLAYSURF)
    all_sprites_list.draw(DISPLAYSURF)
    if event.type==pygame.MOUSEBUTTONDOWN:
        if event.button==3:
            pos=pygame.mouse.get_pos()
            if pos[0]>116 and pos[0]<336 and pos[1]>345 and pos[1]<357:
                striker.rect.x=pos[0]
                striker.rect.y=345
                striker_list.draw(DISPLAYSURF)
                all_sprites_list.draw(DISPLAYSURF)
        elif event.button==1:
            linedrawing(pos)

            

    
            
            
    pygame.display.flip()

