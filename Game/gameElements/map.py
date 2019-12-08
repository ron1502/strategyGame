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

        self.tiles=[]

        

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
        for x in range (15):
            self.tiles[0][x].sType(1)
        for x in range (15):
            if ( x== 0):
                self.tiles[1][x].sType(2)
            elif ( x== 2):
                self.tiles[1][x].sType(3)
            elif ( x== 4):
                self.tiles[1][x].sType(2)
            else:
                self.tiles[1][x].sType(1)
        for x in range (15):
            if ( x== 1):
                self.tiles[2][x].sType(2)
            elif ( x== 2):
                self.tiles[2][x].sType(6)
            elif ( x== 3):
                self.tiles[2][x].sType(5)
            elif ( x== 6):
                self.tiles[2][x].sType(7)
            else:
                self.tiles[2][x].sType(1)
        for x in range (15):
            if ( x== 6):
                self.tiles[3][x].sType(8)
            else:
                self.tiles[3][x].sType(1)
        for x in range (15):
            if ( x == 5):
                self.tiles[4][x].sType(9)
            elif( x == 6):
                self.tiles[4][x].sType(10)
            elif ( x == 7):
                self.tiles[4][x].sType(9)
            else:
                self.tiles[4][x].sType(1)
        for x in range (15):
            if ( x == 6):
                self.tiles[5][x].sType(8)
            else:
                self.tiles[5][x].sType(7)
            

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

    # Gets tile that has been clicked on
    def getSelectedTile(self, x, y):
        for row in self.tiles:
            for tile in row:
                if(tile.mouseInIt(x, y)): return tile
        return None

    def draw(self):
        self.drawTileContent()
        self.drawGridLines()

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
        self.drawImg()

    def update(self):
        pass
    def sType(self, t):
        if (t == 1):
            self.img = self.loadImg(r"\resources\sprites\map\grass.png")
        if (t == 2):
            self.img = self.loadImg(r"\resources\sprites\map\rock1.png")
        if (t == 3):
            self.img = self.loadImg(r"\resources\sprites\map\stair.png")
        if (t == 4):
            self.img = self.loadImg(r"\resources\sprites\map\brigde1.png")
        if (t == 5):
            self.img = self.loadImg(r"\resources\sprites\map\cave.png")    
        if (t == 6):
            self.img = self.loadImg(r"\resources\sprites\map\stair2.png")
        if (t == 7):
            self.img = self.loadImg(r"\resources\sprites\map\water1.png")
        if (t == 8):
            self.img = self.loadImg(r"\resources\sprites\map\water.png")
        if (t == 9):
            self.img = self.loadImg(r"\resources\sprites\map\rock2.png")
        if (t == 10):
            self.img = self.loadImg(r"\resources\sprites\map\water2.png")