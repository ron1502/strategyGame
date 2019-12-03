import pygame
from Game.gameElements.sprite import sprite


#for each type: [0]=their sprite [1]=movement cost of tile [2]=defense value of tile [3]=avoidance value of tile
typeBridge=[" ", 1, 0, -5]
typePlains=[" ", 1, 0, 0]
typeForest=[" ", 2, 1, 10]
typeHill=[" ", 2, 3, 0]
typeRiver=[" ", 100, 0, 0]#river is impassable, take a bridge over it

typeSwitcher = {
    0: typeBridge,
    1: typePlains,
    2: typeForest,
    3: typeHill,
    4: typeRiver 
}

class tile(sprite):

    BGCOLOR = pygame.Color(95, 111, 58)
    SBGCOLOR = pygame.Color(144, 159, 67)
    MAPTOPMARGIN = 0
    MAPLEFTMARGIN = 0
    
    def __init__(self, tType, x, y, w = 60, h = 60, unit = None):
        super().__init__(x, y, w, h)
        self.type = typeSwitcher.get(tType, "nothing")
        self.unit = unit
        self.inRange = 0

        #controlls animation of tile
        self.selected = False
        self.animation = 0

    def tileEmpty(self):
        return self.unit is None

    def isInRange(self, rMov):
        if(rMov-self.type[1]>=0 and (self.tileEmpty() or (not self.unit.isEnemy))):
            return True
        else:
            return False

    def isInRangeEnemy(self, rMov):
        if(rMov-self.type[1]>=0 and (self.tileEmpty() or (self.unit.isEnemy))):
            return True
        else:
            return False

    def setUnit(self, unit):
        self.unit = unit
        self.locateInCenter()
            
        
    # Locates sprite in the center of the Tile
    # Gives x and y possition to unit based tile position
    def locateInCenter(self):
        self.unit.rect.x = self.rect.x
        self.unit.rect.y = self.rect.y
        if(self.unit.rect.w <= self.rect.w):
            if(self.unit.rect.h <= self.rect.h):
                self.unit.rect.x += (self.rect.w - self.unit.rect.w)//2
                self.unit.rect.y += (self.rect.h - self.unit.rect.h)//2
        # Define image scale for cases where sprite is bigger than tile

    def getPlayerCenter(self, w, h):
        x = self.rect.x + (self.rect.w - w)//2
        y = self.rect.y + (self.rect.h - h)//2
        return (x, y)

    def draw(self):
        self.update()
        self.drawSquare()
        if self.unit != None:
            self.unit.draw()

    # Getting coordintes of tiles in map table
    def getRIndex(self):
        return (self.rect.y - tile.MAPTOPMARGIN)//self.rect.h 

    def getCIndex(self):
        return (self.rect.x - tile.MAPLEFTMARGIN)//self.rect.w

    def update(self):
        if(self.selected):
            if(self.animation < 32):
                self.animation += 1
                self.rectColor =  tile.SBGCOLOR
            elif(self.animation < 64):
                self.animation += 1
                self.rectColor = tile.BGCOLOR
            else:
                self.animation = 0
        else:
            self.rectColor = tile.BGCOLOR
#a1=tile(2)
#a2=tile(2)
#a2.unit="John Smith"
#print(a1.type)
#print(a2.type)
#print(a1.unit)
#print(a2.unit) testing
