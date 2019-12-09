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
    
    def __init__(self, mapData):
        super().__init__(0, 0, 0, 0)

        self.tiles = []
        self.items = []

        
        ## Tile initialization (Can be used for the initialization of tiles in from  jsonData)
        # In that case map dimension can be access with no problem through map
        
        for i in range(map.ROWCOUNT):
            yPos = (map.GHEIGHT * i) 
            newRow = []
            for j in range(map.COLUMNCOUNT):
                xPos = (map.GWIDTH * j)
                newRow.append(tile(xPos, yPos, map.GWIDTH, map.GHEIGHT, mapData[i][j]))
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
                if(tile.type >= 4 and tile.collide(sprite)):
                    return True
        return False
    
    # Gets tile that has been clicked on
    def getSelectedTile(self, x, y):
        for row in self.tiles:
            for tile in row:
                if(tile.mouseInIt(x, y)): return tile
        return None

    def getTileAt(self, x, y):
        print("Grid Coordinates ROW: {" + str(y//map.GHEIGHT) + "} COLUMN: {" + str(x//map.GWIDTH) + "}")
        return self.tiles[y//map.GHEIGHT][x//map.GWIDTH]

    def getTiles(self):
        tileArray = []
        for row in self.tiles:
            tileArray += row
        return tileArray

    def draw(self):
        self.drawTileContent()
        self.drawGridLines()
        for item in self.items:
            item.draw()

    def update(self):
        pass

GRASS0 = 0
GRASS1 = 1
GRASS2 = 2
BRIDGE = 3
STAIR0 = 4
STAIR1 = 5
STAIR2 = 6
STAIR3 = 7
WALLWATER0 = 8
WALLWATER1 = 9
WALLWATER2 = 10
WALLWATER3 = 11

ROCK = 4
ROCK2 = 5
CAVE = 6
STILLW = 7
WATER1 = 8
WATER2 = 9


class tile(sprite):
    BGCOLOR = pygame.Color(95, 111, 58)
    SBGCOLOR = pygame.Color(144, 159, 67)
    MAPTOPMARGIN = 0
    MAPLEFTMARGIN = 0

    TYPE = None
    
    def __init__(self, x, y, w, h, tType):
        super().__init__(x, y, w, h)
        if tile.TYPE == None:
            tile.TYPE = []
            stillWater = []
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\Grass0.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\Grass1.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\Grass2.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\bridge.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\stairs0.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\stairs1.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\stairs2.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\stairs3.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\wallWater0.png"))
            tile.TYPE.append(self.loadImg(r"\resources\sprites\map\wallWater1.png"))
        self.type = tType
       # if(self.type == STILLW):  self.img = tile.TYPE[STILLW][0]
        self.img = tile.TYPE[tType]
        
    def getCenter(self, w, h):
        x = self.rect.x + (self.rect.w - w)//2
        y = self.rect.y + (self.rect.h - h)//2
        return (x, y)

    def draw(self):
        if(self.type == STILLW):
            if(self.nextAnimation(1, 300)):
                self.img = tile.TYPE[STILLW][self.animationCount]
        self.drawImg()

    def update(self):
        pass


