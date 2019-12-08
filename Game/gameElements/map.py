from Game.gameElements.sprite import sprite
from Game.gameElements.player import player

import pygame
import random

class map(sprite):
    GRIDCOLOR = pygame.Color(0, 0, 0)
    
    #Grid dimensions
    GHEIGHT = 70
    GWIDTH = 70
    
    #Number of rows and Columns
    ROWCOUNT = 10
    COLUMNCOUNT = 15

    #Map Margin
    TOPMARGIN = 10
    LEFTMARGIN = 65
    
    def __init__(self, filename):
        super().__init__(0, 0, 0, 0)

        self.tiles = []
        self.items = []
        tile.MAPTOPMARGIN = map.TOPMARGIN
        tile.MAPLEFTMARGIN = map.LEFTMARGIN
        
        ## Tile initialization (Can be used for the initialization of tiles in from  jsonData)
        # In that case map dimension can be access with no problem through map
        
        for i in range(map.ROWCOUNT):
            yPos = (map.GHEIGHT * i) 
            newRow = []
            for j in range(map.COLUMNCOUNT):
                xPos = (map.GWIDTH * j)
                newRow.append(tile(1, xPos, yPos, map.GWIDTH, map.GHEIGHT))
            self.tiles.append(newRow)

    def drawGridLines(self):
        yLimit = map.GHEIGHT * map.ROWCOUNT
        xLimit = map.GWIDTH * map.COLUMNCOUNT
        for rowNum in range(map.ROWCOUNT + 1):
            yLinePos = map.GHEIGHT * rowNum
            pygame.draw.line(sprite.screen, map.GRIDCOLOR, (0, yLinePos), (xLimit, yLinePos))
        for colNum in range(map.COLUMNCOUNT + 1):
            xLinePos = map.GWIDTH * colNum
            pygame.draw.line(sprite.screen, map.GRIDCOLOR, (xLinePos,  0), (xLinePos, yLimit))

    ## Can become part of model depending of our needs  ##
    def drawTileContent(self):
        for i in range(map.ROWCOUNT):
            for j in range(map.COLUMNCOUNT):
                self.tiles[i][j].draw()

    def collide(self, sprite):
        for row in self.tiles:
            for tile in row:
                if(tile.type == "Wall" and sprite.collide(sprite)):
                    return True
        return False
    
    # Gets tile that has been clicked on
    def getSelectedTile(self, x, y):
        for row in self.tiles:
            for tile in row:
                if(tile.mouseInIt(x, y)): return tile
        return None

    def draw(self):
        self.drawTileContent()
        self.drawGridLines()
        for item in self.items:
            item.draw()

    def update(self):
        pass

class tile(sprite):
    BGCOLOR = pygame.Color(95, 111, 58)
    SBGCOLOR = pygame.Color(144, 159, 67)
    MAPTOPMARGIN = 0
    MAPLEFTMARGIN = 0
    
    def __init__(self, tType, x, y, w, h, imgSource = None):
        super().__init__(x, y, w, h, imgSource)
        self.type = tType
    
##    def locateInCenter(self):
##        self.unit.rect.x = self.rect.x
##        self.unit.rect.y = self.rect.y
##        if(self.unit.rect.w <= self.rect.w):
##            if(self.unit.rect.h <= self.rect.h):
##                self.unit.rect.x += (self.rect.w - self.unit.rect.w)//2
##                self.unit.rect.y += (self.rect.h - self.unit.rect.h)//2

    def getCenter(self, w, h):
        x = self.rect.x + (self.rect.w - w)//2
        y = self.rect.y + (self.rect.h - h)//2
        return (x, y)

    def draw(self):
        self.drawSquare()

    def update(self):
        pass