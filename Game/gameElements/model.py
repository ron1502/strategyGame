import json
import pygame
from Game.gameElements.sprite import sprite
from Game.gameElements.map import map
from Game.gameElements.unitMenu import unitMenu
from Game.gameElements.button import button
from Game.gameElements.menu import menu
from Game.gameElements.player import player

class model:
    def __init__(self):
        self.sprites = []
        self.run = True
        self.menuSprites = [];
        self.gameSprites = [];
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
        center = self.map.tiles[4][4].getPlayerCenter(50, 37)
        self.player = player(center[0], center[1], 100, 100, 100, 100, 1, 0)
        self.addSprite(self.map)
        self.addSprite(self.unitMenu.getStatsSprite())
        self.addSprite(self.player)

    def setUpMenu(self):
        self.menu = menu()
        self.menuSprites += self.menu.getButtons()
        self.sprites =  self.menuSprites
        
    def addSprite(self, sprite):
        self.sprites.append(sprite)

    def removeSprite(self, sprite):
        self.sprites.remove(sprite)

    def checkClick(self, x, y):
        if self.stage == "GAME":
            tile = self.map.getSelectedTile(x, y)
            if(tile != None and tile.unit == None):
                center = tile.getPlayerCenter(self.player.rect.w, self.player.rect.h)
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
        
    def loadGame(self):
        pass

    def saveGame(self):
        pass

    def update(self):
        # Makes button clicking animation work
        for button in self.unitMenu.getButtons():
            button.update()
        self.player.update()
