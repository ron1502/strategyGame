from Game.gameElements.sprite import sprite
from Game.gameElements.player import player

import pygame
import random
white= (255, 255, 255)

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
                newRow.append(tile(1, xPos, yPos, map.GWIDTH, map.GHEIGHT))
            self.tiles.append(newRow)
        for x in range (15):
            if x== 1:
                self.tiles[0][x].sType(13)
            elif x == 6:
                self.tiles[0][x].sType(55)
            elif x == 4:
                self.tiles[0][x].sType(12)
            elif x == 7 or x == 8 :
                self.tiles[0][x].sType(9)
            elif x == 9 :
                self.tiles[0][x].sType(37)
            elif x ==13 :
                self.tiles[0][x].sType(38)
            elif x == 10 or x==12 or x == 11 :
                self.tiles[0][x].sType(2)
            elif x == 14:
                self.tiles[0][x].sType(13)
            else:
                self.tiles[0][x].sType(1)
        for x in range (15):
            if x == 1:
                self.tiles[1][x].sType(14)
            elif x == 2 or x == 11:
                self.tiles[1][x].sType(12)
            elif x == 4:
                self.tiles[1][x].sType(2)
            elif x == 5:
                self.tiles[1][x].sType(9)
            elif x == 7:
                self.tiles[1][x].sType(39)
            elif x == 8:
                self.tiles[1][x].sType(5)
            elif x == 14:
                self.tiles[1][x].sType(14)
            else:
                self.tiles[1][x].sType(1)
        for x in range (15):
            if ( x== 0 or x == 2):
                self.tiles[2][x].sType(2) 
            elif ( x== 1):
                 self.tiles[2][x].sType(9)
            elif x ==3 :
                self.tiles[2][x].sType(46)
            elif x ==5 :
                self.tiles[2][x].sType(2)
            elif x == 8:
                self.tiles[2][x].sType(17)
            elif x == 9:
                self.tiles[2][x].sType(18)
            elif x == 10:
                self.tiles[2][x].sType(19)
            elif x == 11:
                self.tiles[2][x].sType(20)
            elif x == 12 or x ==13 or x == 14:
                self.tiles[2][x].sType(7)
            else:
                self.tiles[2][x].sType(1)
        for x in range (15):
            if ( x== 1 ):
                self.tiles[3][x].sType(2)
            elif x == 2:
                self.tiles[3][x].sType(57)
            elif x == 3:
                self.tiles[3][x].sType(48)
            elif x == 4:
                self.tiles[3][x].sType(57)
            elif x == 8:
                self.tiles[3][x].sType(21)
            elif x == 9:
                self.tiles[3][x].sType(22)
            elif x == 10:
                self.tiles[3][x].sType(23)
            elif x == 11:
                self.tiles[3][x].sType(24)
            elif x == 12:
                self.tiles[3][x].sType(8)
            else:
                self.tiles[3][x].sType(1)
        for x in range (15):
            if x== 0:
                self.tiles[4][x].sType(49)
            elif ( x== 2):
                self.tiles[4][x].sType(2)
            elif ( x== 3):
                self.tiles[4][x].sType(47)
            elif x == 4:
                self.tiles[4][x].sType(40)
            elif ( x== 6):
                self.tiles[4][x].sType(7)
            elif x == 8:
                self.tiles[4][x].sType(25)
            elif x == 7:
                self.tiles[4][x].sType(50)
            elif x == 9:
                self.tiles[4][x].sType(26)
            elif x == 10:
                self.tiles[4][x].sType(27)
            elif x == 11:
                self.tiles[4][x].sType(28)
            elif x == 12:
                self.tiles[4][x].sType(8)
            else:
                self.tiles[4][x].sType(1)
        for x in range (15):
            if x == 0:
                self.tiles[5][x].sType(43)
            elif x== 1:
                self.tiles[5][x].sType(50)

            elif ( x== 6):
                self.tiles[5][x].sType(8)
            elif x == 8:
                self.tiles[5][x].sType(29)
            elif x == 9:
                self.tiles[5][x].sType(30)
            elif x == 10:
                self.tiles[5][x].sType(31)
            elif x == 11:
                self.tiles[5][x].sType(32)
            elif x == 12:
                self.tiles[5][x].sType(53)
            elif x == 13:
                self.tiles[5][x].sType(54)
            elif x == 14:
                self.tiles[5][x].sType(52)
            else:
                self.tiles[5][x].sType(1)
        for x in range (15):
            
            """if x == 0:
                self.tiles[6][x].sType(16)
            elif x == 1:
                self.tiles[6][x].sType(15)
            elif x == 2:
                self.tiles[6][x].sType(16)
            elif x == 3:
                self.tiles[6][x].sType(15)"""
            if x == 0:
                self.tiles[6][x].sType(44)
            elif x == 4:
                self.tiles[6][x].sType(56)
            elif x == 1:
                self.tiles[6][x].sType(49)
            elif ( x == 5):
                self.tiles[6][x].sType(9)
            elif( x == 6):
                self.tiles[6][x].sType(10)
            elif ( x == 7):
                self.tiles[6][x].sType(9)
            elif x == 12:
                self.tiles[6][x].sType(8)
            else:
                self.tiles[6][x].sType(1)
        for x in range (15):
            if ( x== 9):
                self.tiles[7][x].sType(11)
            elif ( x == 6):
                self.tiles[7][x].sType(8)
            elif x == 12:
                self.tiles[7][x].sType(8)
            else:
                self.tiles[7][x].sType(7)
        for x in range (15):
            if ( x== 8 or x==9 or x==10):
                self.tiles[8][x].sType(33)
           # elif x == 3 or x== 2 or x ==1 or x==0:
            #    self.tiles[8][x].sType(58)
            elif x == 7:
                self.tiles[8][x].sType(35)
            elif x == 11:
                self.tiles[8][x].sType(36)
            elif x == 12:
                self.tiles[8][x].sType(8)
            else:
                self.tiles[8][x].sType(8)
        for x in range (15):
            if (x==8 or x==9 or x==10):
                self.tiles[9][x].sType(34)
            elif (x == 7):
                self.tiles[9][x].sType(42)
            elif (x == 11):
                self.tiles[9][x].sType(41)
            elif x == 12:
                self.tiles[9][x].sType(8)
            elif x == 4 or x == 5 or x== 6 or x == 4 or x == 3 or x== 2 or x ==1 or x==0:
                self.tiles[9][x].sType(58)
            else:
                self.tiles[9][x].sType(8)
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
        if (t == 11):
            self.img = self.loadImg(r"\resources\sprites\map\brigde.png")
        if (t == 12):
            self.img = self.loadImg(r"\resources\sprites\map\flower.png")
        if (t == 13):
            self.img = self.loadImg(r"\resources\sprites\map\tree1.png")
        if (t == 14):
            self.img = self.loadImg(r"\resources\sprites\map\tree2.png")
        if (t == 15):
            self.img = self.loadImg(r"\resources\sprites\map\fence1.png")
        if (t == 16):
            self.img = self.loadImg(r"\resources\sprites\map\fence2.png")
        if (t == 17):
            self.img = self.loadImg(r"\resources\sprites\map\1.png")
        if (t == 18):
            self.img = self.loadImg(r"\resources\sprites\map\2.png")
        if (t == 19):
            self.img = self.loadImg(r"\resources\sprites\map\3.png")
        if (t == 20):
            self.img = self.loadImg(r"\resources\sprites\map\4.png")
        if (t == 21):
            self.img = self.loadImg(r"\resources\sprites\map\5.png")
        if (t == 22):
            self.img = self.loadImg(r"\resources\sprites\map\6.png")
        if (t == 23):
            self.img = self.loadImg(r"\resources\sprites\map\7.png")
        if (t == 24):
            self.img = self.loadImg(r"\resources\sprites\map\8.png")
        if (t == 25):
            self.img = self.loadImg(r"\resources\sprites\map\9.png")
        if (t == 26):
            self.img = self.loadImg(r"\resources\sprites\map\10.png")
        if (t == 27):
            self.img = self.loadImg(r"\resources\sprites\map\11.png")
        if (t == 28):
            self.img = self.loadImg(r"\resources\sprites\map\12.png")
        if (t == 29):
            self.img = self.loadImg(r"\resources\sprites\map\13.png")
        if (t == 30):
            self.img = self.loadImg(r"\resources\sprites\map\14.png")
        if (t == 31):
            self.img = self.loadImg(r"\resources\sprites\map\15.png")
        if (t == 32):
            self.img = self.loadImg(r"\resources\sprites\map\16.png")
        if (t == 33):
            self.img = self.loadImg(r"\resources\sprites\map\17.png")
        if (t == 34):
            self.img = self.loadImg(r"\resources\sprites\map\18.png")
        if (t == 35):
            self.img = self.loadImg(r"\resources\sprites\map\19.png")
        if (t == 36):
            self.img = self.loadImg(r"\resources\sprites\map\20.png")
        if (t == 37):
            self.img = self.loadImg(r"\resources\sprites\map\21.png")
        if (t == 38):
            self.img = self.loadImg(r"\resources\sprites\map\22.png")
        if (t == 39):
            self.img = self.loadImg(r"\resources\sprites\map\23.png")
        if (t == 40):
            self.img = self.loadImg(r"\resources\sprites\map\24.png")
        if (t == 41):
            self.img = self.loadImg(r"\resources\sprites\map\25.png")
        if (t == 42):
            self.img = self.loadImg(r"\resources\sprites\map\26.png")
        if (t == 43):
            self.img = self.loadImg(r"\resources\sprites\map\27.png")
        if (t == 44):
            self.img = self.loadImg(r"\resources\sprites\map\28.png")
        if (t == 45):
            self.img = self.loadImg(r"\resources\sprites\map\29.png")
        if (t == 46):
            self.img = self.loadImg(r"\resources\sprites\map\30.png")
        if (t == 47):
            self.img = self.loadImg(r"\resources\sprites\map\31.png")
        if (t == 48):
            self.img = self.loadImg(r"\resources\sprites\map\32.png")
        if (t == 49):
            self.img = self.loadImg(r"\resources\sprites\map\33.png")
        if (t == 50):
            self.img = self.loadImg(r"\resources\sprites\map\34.png")
        if (t == 51):
            self.img = self.loadImg(r"\resources\sprites\map\35.png")
        if (t == 52):
            self.img = self.loadImg(r"\resources\sprites\map\36.png")
        if (t == 53):
            self.img = self.loadImg(r"\resources\sprites\map\37.png")
        if (t == 54):
            self.img = self.loadImg(r"\resources\sprites\map\38.png")
        if (t == 55):
            self.img = self.loadImg(r"\resources\sprites\map\39.png")
        if (t == 56):
            self.img = self.loadImg(r"\resources\sprites\map\40.png")
        if (t == 57):
            self.img = self.loadImg(r"\resources\sprites\map\41.png")
        if (t == 58):
            self.img = self.loadImg(r"\resources\sprites\map\42.png")
