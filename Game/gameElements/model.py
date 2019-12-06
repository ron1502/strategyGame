import json
import pygame
from Game.gameElements.sprite import sprite
from Game.gameElements.map import map
from Game.gameElements.button import button
from Game.gameElements.menu import menu

from Game.gameElements.player import player
from Game.gameElements.enemy import worm
from Game.gameElements.enemy import dragon
from Game.gameElements.particles import particles

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
        self.items = self.map.items
        playerCenter = self.map.tiles[4][4].getCenter(50, 37)
        self.player = player(playerCenter[0], playerCenter[1], 10, 100, 100, 1, 0)

        wormCenter =  self.map.tiles[3][2].getCenter(64, 64)
        self.worm = worm(wormCenter[0], wormCenter[1], 64, 64)

        wormCenter =  self.map.tiles[9][4].getCenter(64, 64)
        self.worm2 =  worm(wormCenter[0], wormCenter[1], 64, 64)

        wormCenter =  self.map.tiles[1][10].getCenter(64, 64)
        self.worm3 = worm(wormCenter[0], wormCenter[1], 64, 64)


        dragonCenter = self.map.tiles[5][11].getCenter(70, 70)
        self.dragon = dragon(dragonCenter[0], dragonCenter[1], 70, 70, self.map)

        dragonCenter = self.map.tiles[3][1].getCenter(70, 70)
        self.dragon2 = dragon(dragonCenter[0], dragonCenter[1], 70, 70, self.map)

        particleCenter = self.map.tiles[7][10].getCenter(70, 70)
        self.particles = particles(particleCenter[0], particleCenter[1], 70, 70)

        particleCenter = self.map.tiles[4][2].getCenter(70, 70)
        self.particles2 = particles(particleCenter[0], particleCenter[1], 70, 70)

        particleCenter = self.map.tiles[5][5].getCenter(70, 70)
        self.particles3 = particles(particleCenter[0], particleCenter[1], 70, 70)

        particleCenter = self.map.tiles[2][11].getCenter(70, 70)
        self.particles4 = particles(particleCenter[0], particleCenter[1], 70, 70)
        
        self.enemies.append(self.worm)
        self.enemies.append(self.worm2)
        self.enemies.append(self.worm3)
        self.enemies.append(self.dragon)
        self.enemies.append(self.dragon2)

        self.addSprite(self.map)
        self.addSprite(self.player)
        self.addSprite(self.worm)
        self.addSprite(self.worm2)
        self.addSprite(self.worm3)
        self.addSprite(self.dragon)
        self.addSprite(self.dragon2)
        self.addSprite(self.particles)
        self.addSprite(self.particles2)
        self.addSprite(self.particles3)
        self.addSprite(self.particles4)



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
            if(sprite.type == "Wall"):
                self.player.collide(x, y, True)
                #DRAKE: Wall sound collision can play here
        for enemy in self.enemies:
            if(not enemy.alive):
                item =  enemy.dropItem()
                self.gameSprites.remove(enemy)
                self.enemies.remove(enemy)
                if(item != None):
                    self.items.append(item)

            elif(self.player.collide(enemy) and not enemy.isDying):
                if(enemy.isAttacking and enemy.hitAgain()):
                    self.player.receiveAttack(enemy.attackDamage)
                    #DRAKE: Payer being attacked 
                if(self.player.attacking):
                    enemy.receiveAttack(self.player.attackDamage)
                    #DRAKE: Enemy being attacked

                    
    def checkClick(self, x, y):
        if self.stage == "GAME":
            for item in self.items:
                if(item.mouseInIt(x, y)):
                    self.player.heal(item.heallingEffect())
                    self.items.remove(item)
                    #DRAKE: Healing sound can play here
                    return

            tile = self.map.getSelectedTile(x, y)
            center = tile.getCenter(self.player.rect.w, self.player.rect.h)
            self.player.moveTo(center[0], center[1])


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
            for sprite in self.sprites:
                sprite.update()
