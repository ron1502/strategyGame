import pygame
import time

pygame.init()

#---WIDTH,HEIGHT,COLORS,MEASUREMENTS SET---

black=(0,0,0)
white=(255,255,255)
light_grey=(190, 193, 198)
dark_grey=(77, 77, 77)

red=(200,0,0)
green=(0,200,0)
blue=(0,0,200)

bright_green=(102, 255, 102)
bright_red=(255, 77, 77)

#--START SET---
gameDisplay= pygame.display.set_mode((480,480))
clock=pygame.time.Clock()


def text_objects(text, font):
    textSurface=font.render(text,True,dark_grey)
    return textSurface,textSurface.get_rect()
    
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0]==1 and action !=None:
            action()
            pass
            
             
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))

        #TEXT ON BUTTON
    smallText=pygame.font.SysFont('Berlin Sans FB',20)
    textSurf, textRect=text_objects(msg,smallText)
    textRect.center=((x+(w/2)),(y+h/2))
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def game_intro(width, height, function):
    gameDisplay= pygame.display.set_mode((width, height))
    
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()     
       

        #-INTRO DISPLAY-
        gameDisplay.fill(white)

        #---BUTTON--
        button("GO",200,150,100,50,light_grey,white,function)
        button("QUIT",200,250,100,50,light_grey,white,quitgame) 

        
        pygame.display.update()
        clock.tick(60)




