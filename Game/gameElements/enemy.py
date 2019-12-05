import random
import pygame
from Game.gameElements.sprite import sprite
from Game.gameElements.lifeBar import lifeBar


WORMHP = 30

class worm(sprite):
    def __init__(self, x, y, w, h, tiles, xT, yT):
        super().__init__(x, y, w, h)
        self.attack = 10
        self.idle = [self.loadImg(r"\resources\sprites\worm\idle\00.png"), self.loadImg(r"\resources\sprites\worm\idle\01.png"),
                     self.loadImg(r"\resources\sprites\worm\idle\02.png"), self.loadImg(r"\resources\sprites\worm\idle\03.png"),
                     self.loadImg(r"\resources\sprites\worm\idle\04.png"), self.loadImg(r"\resources\sprites\worm\idle\05.png"),
                     self.loadImg(r"\resources\sprites\worm\idle\06.png"), self.loadImg(r"\resources\sprites\worm\idle\07.png")]
        self.idleDirt = self.loadImg(r"\resources\sprites\worm\dirt\idle.png");

        self.dying = [self.loadImg(r"\resources\sprites\worm\dying\00.png"), self.loadImg(r"\resources\sprites\worm\dying\01.png"),
                     self.loadImg(r"\resources\sprites\worm\dying\02.png"), self.loadImg(r"\resources\sprites\worm\dying\03.png"),
                     self.loadImg(r"\resources\sprites\worm\dying\04.png"), self.loadImg(r"\resources\sprites\worm\dying\05.png")]

        self.dyingDirt = [self.loadImg(r"\resources\sprites\worm\dying\d00.png"), self.loadImg(r"\resources\sprites\worm\dying\d01.png"),
                     self.loadImg(r"\resources\sprites\worm\dying\d02.png"), self.loadImg(r"\resources\sprites\worm\dying\d03.png"),
                     self.loadImg(r"\resources\sprites\worm\dying\d04.png"), self.loadImg(r"\resources\sprites\worm\dying\d05.png")]

        self.dirt = self.idleDirt
        self.animationCount = 0
        self.hp = WORMHP
        self.img = self.idle[0]
        self.lifeBar = lifeBar(self.rect, self.hp)

        #Tile Data
        self.tiles =  tiles
        #Position in tiles
        self.xT = xT
        self.yT = yT
        
        self.isIdle = True
        self.isJumping = False
        self.isDying =  False
        
        self.lastJump = pygame.time.get_ticks()
        self.alive =  True
        
    def jump(self):
        return False
    
    def receiveAttack(self, damage):
        self.hp -= damage
        if(self.hp <= 0):
            self.animationCount = 0
            self.isDying = True
            self.isIdle = False
            print("Dyin has started")
            print(self.animationCount)
            #DRAKE: Dying sound
            
    def update(self):
        self.lifeBar.update(self.rect, self.hp)
        if(pygame.time.get_ticks() -  self.lastJump >= 2000):
            self.lastJump = pygame.time.get_ticks()
            if(self.jump()):
                self.isJumping =  True
                self.isIdle =  False
            
        if(self.isIdle):
            if(self.nextAnimation(7, 100)):
                self.img = self.idle[self.animationCount]
                self.dirt = self.idleDirt
        elif(self.isJumping):
            pass
        elif(self.isDying):
            if(self.nextAnimation(6, 100)):
                if(self.animationCount == 6):
                    self.isDying = False
                    self.alive = False
                else:
                    print("Animating dead")
                    self.img = self.dying[self.animationCount]
                    self.dirt = self.dyingDirt[self.animationCount]

    def draw(self):
        self.lifeBar.draw()
        self.drawImg()
        sprite.screen.blit(self.dirt, self.rect)

