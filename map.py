from tile import *

def enemiesEliminated(self):#example clear condition
    return self.enemies is 0
clearSwitcher = {
    0: enemiesEliminated
}
class map:

    
    
    def __init__(self, filename):
        #in final version this will probably load the file at filename and initialize all of this
        #for testing purposes I set it all manually for now
        self.height=5
        self.width=5
        self.enemies=0
        self.clearCondition=0
        self.tiles=[[]]
        self.turn=1 #it's 1 when player's turn 2 when enemy's turn.
        self.rangeTable=[0]*self.width
        for i in range(self.width):
            self.rangeTable[i]=[0]*self.height
        #print(self.rangeTable)

    def isClear(self):
        func=clearSwitcher.get(self.clearCondition, "nothing")
        return func(self)

    #this will recursively set up a table representing what tiles a unit may move into
    #a 1 means that unit can move there a 2 means that unit cannot move there
    def constructRangeTable(self, x, y, MOV): #x refers to what row the unit is in y is what column it's in.
        self.rangeTable[x][y]=1 #obviously a unit is allowed to stay where it is, "move" to its own location.
        if x-1>=0:
            if self.tiles[x-1][y].isInRange(MOV):
                nMOV=MOV-self.tiles[x-1][y].type[1]
                self.constructRangeTable(x-1, y, nMOV)
        if x+1<self.height:
            if self.tiles[x+1][y].isInRange(MOV):
                nMOV=MOV-self.tiles[x+1][y].type[1]
                self.constructRangeTable(x+1, y, nMOV)
        if y-1>=0:
            if self.tiles[x][y-1].isInRange(MOV):
                nMOV=MOV-self.tiles[x][y-1].type[1]
                self.constructRangeTable(x, y-1, nMOV)
        if y+1<self.width:
            if self.tiles[x][y+1].isInRange(MOV):
                nMOV=MOV-self.tiles[x][y+1].type[1]
                self.constructRangeTable(x, y+1, nMOV)

    def clearRangeTable(self):
        self.rangeTable=[0]*self.width
        for i in range(self.width):
            self.rangeTable[i]=[0]*self.height
            
        
a=map("level1.txt") #note that you have to manually set the height and width in the constructor right now
#if you don't do this rangeTable will not be correctly declared in the initializor
#this will not be a problem in the final version as height and width will be read from a file before setting up rangeTable
'''a.height=5
a.width=5
a.tiles=[[tile(1), tile(1), tile(1), tile(1), tile(1)],
         [tile(1), tile(1), tile(1), tile(1), tile(1)],
         [tile(1), tile(1), tile(1), tile(1), tile(1)],
         [tile(1), tile(1), tile(1), tile(1), tile(1)],
         [tile(1), tile(1), tile(1), tile(1), tile(1)]]
a.constructRangeTable(2, 2, 2)#A unit with 2 movement starting from the middle tile
for i in range(5):
    print(a.rangeTable[i])

a.tiles[2][3].unit=10
a.clearRangeTable()
a.constructRangeTable(2, 2, 2) #the same move but now a unit is to the right of our unit.
print("")
for i in range(5):
    print(a.rangeTable[i])
'''
#a.enemies=1
#print(a.isClear())
#a.enemies-=1
#print(a.isClear())
