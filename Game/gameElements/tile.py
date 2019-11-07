from unit import *

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

class tile:
    def __init__(self, tType):
        self.type=typeSwitcher.get(tType, "nothing")
        self.unit=None #equivalent to NULL. Refers to what unit is in the tile
        self.inRange=0

    def tileEmpty(self):
        if self.unit is None:
            return True
        else:
            return False

    def isInRange(self, rMov):
        if(rMov-self.type[1]>=0 and self.tileEmpty()):
            return True
        else:
            return False

    def tileEmpty(self):
        if self.unit is None:
            return true
        else:
            return false


#a1=tile(2)
#a2=tile(2)
#a2.unit="John Smith"
#print(a1.type)
#print(a2.type)
#print(a1.unit)
#print(a2.unit) testing
