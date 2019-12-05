import json
import pygame
from Game.gameElements.sprite import sprite
from Game.gameElements.map import map
from Game.gameElements.unitMenu import unitMenu
from Game.gameElements.button import button
from Game.gameElements.menu import menu
from Game.gameElements.player import player
from Game.gameElements.enemy import worm

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
        self.unitMenu = unitMenu(830, 0, 250, 720)
        self.map = map("")

        playerCenter = self.map.tiles[4][4].getCenter(50, 37)
        self.player = player(playerCenter[0], playerCenter[1], 100, 10, 100, 100, 1, 0)

        wormCenter =  self.map.tiles[3][2].getCenter(64, 64)
        self.worm = worm(wormCenter[0], wormCenter[1], 64, 64, self.map.tiles, 3, 2)
        self.enemies.append(self.worm)
        self.addSprite(self.map)
        self.addSprite(self.player)
        self.addSprite(self.worm)

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
        if(self.player.damage):
            self.player.damage = False
            for enemy in self.enemies:
                if(self.player.collide(enemy) and not enemy.isDying):
                    enemy.receiveAttack(self.player.attackDamage)
                if(not enemy.alive):
                    self.gameSprites.remove(enemy)
                    self.enemies.remove(enemy)


                    
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
        # Makes button clicking animation work
        self.checkCollision()
        for enemy in self.enemies:
            enemy.update()
        self.player.update()
