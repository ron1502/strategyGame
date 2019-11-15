from Game.gameElements.tile import tile
from Game.gameElements.sprite import sprite
from Game.gameElements.unit import Unit

import pygame

def enemiesEliminated(self):#example clear condition
    return self.enemies is 0
clearSwitcher = {
    0: enemiesEliminated
}


class map(sprite):
    GRIDCOLOR = pygame.Color(0, 0, 0)
    
    #Grid dimensions
    GHEIGHT = 50
    GWIDTH = 50
    
    #Number of rows and Columns
    ROWCOUNT = 10
    COLUMNCOUNT = 10

    #Map Margin
    TOPMARGIN = 110
    LEFTMARGIN = 100
    
    def __init__(self, filename):
        super().__init__(0, 0, 0, 0)

        self.tiles=[]
        
        ## Tile initialization (Can be used for the initialization of tiles in from  jsonData)
        # In that case map dimension can be access with no problem through map
        
        for i in range(map.ROWCOUNT):
            yPos = (map.GHEIGHT * i) + map.TOPMARGIN
            newRow = []
            for j in range(map.COLUMNCOUNT):
                xPos = (map.GWIDTH * j) + map.LEFTMARGIN
                newRow.append(tile(1, xPos, yPos))
            self.tiles.append(newRow)

        ## Adding units to Tiles
        yPos = (self.GHEIGHT * 2) + map.TOPMARGIN
        xPos = (self.GWIDTH * 4) + map.LEFTMARGIN
        newUnit = Unit(xPos, yPos, 50, 50, r"\resources\sprites\link.png", "OK BOOMER", 100, 100, 100, 100, 100, 100, 100)
        self.tiles[2][4].setUnit(newUnit)
        print(str(self.tiles[2][4].unit))
            
        self.enemies=0
        self.clearCondition=0
        self.turn=1 #it's 1 when player's turn 2 when enemy's turn.
        self.rangeTable=[0]* map.ROWCOUNT
        for i in range(map.ROWCOUNT):
            self.rangeTable[i]=[0]*map.COLUMNCOUNT
        #print(self.rangeTable)

    def render(self):
        pass

    def isClear(self):
        func=clearSwitcher.get(self.clearCondition, "nothing")
        return func(self)

    #recursively set up a table representing what tiles a unit may move into
    #1 means that unit can move there, 0 means that unit cannot move there
    def constructRangeTable(self, x, y, MOV): #x refers to what row the unit is in, y is what column it's in.
        if self.tiles[x][y].tileEmpty():
            self.rangeTable[x][y]=1 #a unit is allowed to stay where it is, "move" to its own location.
        if x-1>=0:
            if self.tiles[x-1][y].isInRange(MOV):
                nMOV=MOV-self.tiles[x-1][y].type[1]
                self.constructRangeTable(x-1, y, nMOV)
                '''recursively there is no difference between moving one
                space, and being in that space from the start with [movement cost] less movement points'''
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

    def drawGridLines(self):
        yLimit = map.GHEIGHT * map.ROWCOUNT + map.TOPMARGIN
        xLimit = map.GWIDTH * map.COLUMNCOUNT + map.LEFTMARGIN
        for rowNum in range(map.ROWCOUNT + 1):
            yLinePos = map.GHEIGHT * rowNum + map.TOPMARGIN
            pygame.draw.line(sprite.screen, map.GRIDCOLOR, (map.LEFTMARGIN, yLinePos), (xLimit, yLinePos))
        for colNum in range(map.COLUMNCOUNT + 1):
            xLinePos = map.GWIDTH * colNum + map.LEFTMARGIN
            pygame.draw.line(sprite.screen, map.GRIDCOLOR, (xLinePos,  map.TOPMARGIN), (xLinePos, yLimit))

    def drawTileContent(self):
        for i in range(map.ROWCOUNT):
            for j in range(map.COLUMNCOUNT):
                self.tiles[i][j].draw()
                
    def draw(self):
        self.drawTileContent()
        self.drawGridLines()

        




            
            
"""      
a=map("level1.txt") #note that you have to manually set the height and width in the constructor right now
#if you don't do this rangeTable will not be correctly declared in the initializor
#this will not be a problem in the final version as height and width will be read from a file before setting up rangeTable
a.height=5
a.width=5
a.tiles=[[tile(1), tile(1), tile(1), tile(1), tile(1)],
         [tile(1), tile(1), tile(1), tile(1), tile(1)],
         [tile(1), tile(1), tile(1), tile(1), tile(1)],
         [tile(1), tile(1), tile(1), tile(1), tile(1)],
         [tile(1), tile(1), tile(1), tile(1), tile(1)]]
a.constructRangeTable(2, 2, 2)#A unit with 2 movement starting from the middle tile
for i in range(5):
    print(a.rangeTable[i])

a.tiles[2][3].unit=Unit("Test.jpg", "Test Description", 0, 1, 2, 3, 4, 5, 6)
a.clearRangeTable()
a.constructRangeTable(2, 2, 2) #the same move but now a unit is to the right of our unit.
print("")
for i in range(5):
    print(a.rangeTable[i])

**/        
#a=map("level1.txt")
#a.enemies=1
#print(a.isClear())
#a.enemies-=1
#print(a.isClear())
"""
