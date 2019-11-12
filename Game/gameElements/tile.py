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
    def __init__(self, tType, x, y, w, h, unit = None):
        super().__init__(x, y, w, h)
        self.type = typeSwitcher.get(tType, "nothing")
        self.unit = unit
        self.inRange = 0

    def tileEmpty(self):
        if self.unit is None:
            return True
        else:
            return False

    def isInRange(self, rMov):
        if(rMov-self.type[1]>=0 and (self.tileEmpty() or (not self.unit.isEnemy))):
            return True
        else:
            return False

    def tileEmpty(self):
        if self.unit is None:
            return True
        else:
            return False

    def setUnit(self, unit):
        self.unit = unit
        self.locateInCenter(unit)

    # Locates sprite in the center og the Tile
    def locateInCenter(self, unit):
        if(unit.rect.w <= self.rect.w):
            if(unit.rect.h <= self.rect.h):
                unit.rect.x += (self.rect.w - unit.rect.w)//2
                unit.rect.y += (self.rect.h - unit.rect.h)//2
                
        # Define image scale for cases where sprite is bigger than tile

    def draw(self):
        self.drawSquare()
        if self.unit != None:
            self.unit.draw()

#a1=tile(2)
#a2=tile(2)
#a2.unit="John Smith"
#print(a1.type)
#print(a2.type)
#print(a1.unit)
#print(a2.unit) testing
