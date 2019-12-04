import random
import pygame
from Game.gameElements.sprite import sprite


class worm(sprite):
    def __init__(self, x, y, w, h, tiles, xT, yT):
        super().__init__(x, y, w, h)
        self.attack = 10
        self.idle = [self.loadImg(r"\resources\sprites\worm\idle\00.png"), self.loadImg(r"\resources\sprites\worm\idle\01.png"),
                     self.loadImg(r"\resources\sprites\worm\idle\02.png"), self.loadImg(r"\resources\sprites\worm\idle\03.png"),
                     self.loadImg(r"\resources\sprites\worm\idle\04.png"), self.loadImg(r"\resources\sprites\worm\idle\05.png"),
                     self.loadImg(r"\resources\sprites\worm\idle\06.png"), self.loadImg(r"\resources\sprites\worm\idle\07.png")]
        self.idleDirt = self.loadImg(r"\resources\sprites\worm\dirt\idle.png");

        self.dirt = self.idleDirt
        self.animationCount = 0

        self.img = self.idle[0]

        #Tile Data
        self.tiles =  tiles
        #Position in tiles
        self.xT = xT
        self.yT = yT
        self.isIdle = True
        self.isJumping = False
        self.lastJump = pygame.time.get_ticks()
        self.alive =  True
        
    def jump(self):
        return False
    def update(self):
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


    def draw(self):
        self.drawImg()
        sprite.screen.blit(self.dirt, self.rect)

