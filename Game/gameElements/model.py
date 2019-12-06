import json
import pygame
from Game.gameElements.sprite import sprite
from Game.gameElements.map import map
from Game.gameElements.button import button
from Game.gameElements.menu import menu

from Game.gameElements.player import player
from Game.gameElements.enemy import worm
from Game.gameElements.enemy import dragon

class model:
    def __init__(self):
        self.sprites = []
        self.run = True
        self.menuSprites = []
        self.gameSprites = []
        self.enemies = []
        self.stage = "MENU"

        self.setUpGame()
        self.setUpMenu()
        
        self.selectedTile = None
        self.tileControlledUnit = None
        self.tileDefendingUnit = None

    def setUpGame(self):
        ## Here Loading can be perform
        self.sprites = self.gameSprites
        self.map = map("")

        playerCenter = self.map.tiles[4][4].getCenter(50, 37)
        self.player = player(playerCenter[0], playerCenter[1], 100, 10, 100, 100, 1, 0)

        wormCenter =  self.map.tiles[3][2].getCenter(64, 64)
        self.worm = worm(wormCenter[0], wormCenter[1], 64, 64)

        wormCenter =  self.map.tiles[9][4].getCenter(64, 64)
        self.worm2 =  worm(wormCenter[0], wormCenter[1], 64, 64)

        dragonCenter = self.map.tiles[5][11].getCenter(70, 70)
        self.dragon = dragon(dragonCenter[0], dragonCenter[1], 70, 70, self.map)
        
        self.enemies.append(self.worm)
        self.enemies.append(self.worm2)
        self.enemies.append(self.dragon)

        self.addSprite(self.map)
        self.addSprite(self.player)
        self.addSprite(self.worm)
        self.addSprite(self.worm2)
        self.addSprite(self.dragon)


    def setUpMenu(self):
        self.menu = menu()
        self.menuSprites += self.menu.getButtons()
        self.sprites =  self.menuSprites
        
    def addSprite(self, sprite):
        self.sprites.append(sprite)

    def removeSprite(self, sprite):
        self.sprites.remove(sprite)

    def checkCollision(self):
        #Attacking Enemy
        for sprite in self.sprites:
            if(sprite.type == "wall"):
                self.player.collide(x, y, True)
                #DRAKE: Wall sound collision can play here
        for enemy in self.enemies:
            if(not enemy.alive):
                self.gameSprites.remove(enemy)
                self.enemies.remove(enemy)
            elif(self.player.collide(enemy) and not enemy.isDying):
                if(enemy.isAttacking and enemy.hitAgain()):
                    self.player.receiveAttack(enemy.attackDamage)
                    #DRAKE: Payer being attacked 
                if(self.player.damage):
                    self.player.damage = False
                    enemy.receiveAttack(self.player.attackDamage)
                    #DRAKE: Enemy being attacked 

                    
    def checkClick(self, x, y):
        if self.stage == "GAME":
            tile = self.map.getSelectedTile(x, y)
            center = tile.getCenter(self.player.rect.w, self.player.rect.h)
            self.player.moveTo(center[0], center[1]);

        else: ## Menu is running
            for sprt in self.sprites:
                if (isinstance(sprt, button)):
                    if(sprt.checkClick(x, y)):
                        if(self.menu.action == "G"):
                            self.stage = "GAME"
                            self.sprites = self.gameSprites
                        elif(self.menu.action == "Q"):
                            self.quitGame()
    def quitGame(self):
        self.run = False
        
    def update(self):
        if(self.stage == "GAME"):
            self.checkCollision()
            for enemy in self.enemies:
                enemy.update()
            self.player.update()