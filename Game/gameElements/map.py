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
    GHEIGHT = 70
    GWIDTH = 70
    
    #Number of rows and Columns
    ROWCOUNT = 10
    COLUMNCOUNT = 10

    #Map Margin
    TOPMARGIN = 10
    LEFTMARGIN = 65
    
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
                newRow.append(tile(1, xPos, yPos, map.GWIDTH, map.GHEIGHT))
            self.tiles.append(newRow)

        ## Adding testing units to Tiles
        newUnit = Unit(0, 0, 50, 50, r"\resources\sprites\link.png", "OK BOOMER", 100, 100, 100, 100, 100, 100, 100)
        self.tiles[2][4].setUnit(newUnit)
        print(str(self.tiles[2][4].unit))
            
        self.enemies=0
        self.clearCondition=0
        self.turn=1 #it's 1 when player's turn 2 when enemy's turn.
        self.rangeTable=[0] * map.ROWCOUNT
        for i in range(map.ROWCOUNT):
            self.rangeTable[i]=[0]*map.COLUMNCOUNT

        self.atkRangeTable=[0] * map.ROWCOUNT
        for i in range(self.width):
            self.atkRangeTable[i]=[0]*map.COLUMNCOUNT

        self.enemyCanAttack=False #This is messy Hayes-code to make the program run more efficiently

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
        atkRange=1
        if (x-atkRange)>=0:
            if not(self.tiles[x-atkRange][y].tileEmpty()):
                if (self.tiles[x-atkRange][y].unit.isEnemy):
                    self.atkRangeTable[x-atkRange][y]=1
        if (x+atkRange)<self.height:
            if not(self.tiles[x+atkRange][y].tileEmpty()):
                if (self.tiles[x+atkRange][y].unit.isEnemy):
                    self.atkRangeTable[x+atkRange][y]=1
        if (y-atkRange)>=0:
            if not(self.tiles[x][y-atkRange].tileEmpty()):
                if (self.tiles[x][y-atkRange].unit.isEnemy):
                    self.atkRangeTable[x][y-atkRange]=1
        if (y+atkRange)<self.width:
            if not(self.tiles[x][y+atkRange].tileEmpty()):
                if (self.tiles[x][y+atkRange].unit.isEnemy):
                    self.atkRangeTable[x][y+atkRange]=1
            
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

    def constructEnemyRangeTable(self, x, y, MOV, atkRange): #It was faster to just copy the other one with slight modifications
        if self.tiles[x][y].tileEmpty():
            self.rangeTable[x][y]=1 #a unit is allowed to stay where it is, "move" to its own location.
        #calculate attack range table
        if (x-atkRange)>=0:
            if not(self.tiles[x-atkRange][y].tileEmpty()):
                if not(self.tiles[x-atkRange][y].unit.isEnemy):
                    self.atkRangeTable[x-atkRange][y]=1
                    self.enemyCanAttack=True
        if (x+atkRange)<self.height:
            if not(self.tiles[x+atkRange][y].tileEmpty()):
                if not(self.tiles[x+atkRange][y].unit.isEnemy):
                    self.atkRangeTable[x+atkRange][y]=1
                    self.enemyCanAttack=True
        if (y-atkRange)>=0:
            if not(self.tiles[x][y-atkRange].tileEmpty()):
                if not(self.tiles[x][y-atkRange].unit.isEnemy):
                    self.atkRangeTable[x][y-atkRange]=1
                    self.enemyCanAttack=True
        if (y+atkRange)<self.width:
            if not(self.tiles[x][y+atkRange].tileEmpty()):
                if not(self.tiles[x][y+atkRange].unit.isEnemy):
                    self.atkRangeTable[x][y+atkRange]=1
                    self.enemyCanAttack=True
        #calculate movement table            
        if x-1>=0:
            if self.tiles[x-1][y].isInRangeEnemy(MOV):
                nMOV=MOV-self.tiles[x-1][y].type[1]
                self.constructEnemyRangeTable(x-1, y, nMOV, 1)
                '''recursively there is no difference between moving one
                space, and being in that space from the start with [movement cost] less movement points'''
        if x+1<self.height:
            if self.tiles[x+1][y].isInRangeEnemy(MOV):
                nMOV=MOV-self.tiles[x+1][y].type[1]
                self.constructEnemyRangeTable(x+1, y, nMOV, 1)
        if y-1>=0:
            if self.tiles[x][y-1].isInRangeEnemy(MOV):
                nMOV=MOV-self.tiles[x][y-1].type[1]
                self.constructEnemyRangeTable(x, y-1, nMOV, 1)
        if y+1<self.width:
            if self.tiles[x][y+1].isInRangeEnemy(MOV):
                nMOV=MOV-self.tiles[x][y+1].type[1]
                self.constructEnemyRangeTable(x, y+1, nMOV, 1)
    

    def clearRangeTables(self):
        self.rangeTable=[0]*self.width
        for i in range(self.width):
            self.rangeTable[i]=[0]*self.height
        self.enemyCanAttack=False

    def drawGridLines(self):
        yLimit = map.GHEIGHT * map.ROWCOUNT + map.TOPMARGIN
        xLimit = map.GWIDTH * map.COLUMNCOUNT + map.LEFTMARGIN
        for rowNum in range(map.ROWCOUNT + 1):
            yLinePos = map.GHEIGHT * rowNum + map.TOPMARGIN
            pygame.draw.line(sprite.screen, map.GRIDCOLOR, (map.LEFTMARGIN, yLinePos), (xLimit, yLinePos))
        for colNum in range(map.COLUMNCOUNT + 1):
            xLinePos = map.GWIDTH * colNum + map.LEFTMARGIN
            pygame.draw.line(sprite.screen, map.GRIDCOLOR, (xLinePos,  map.TOPMARGIN), (xLinePos, yLimit))

    ## Can become part of model depending of out needs  ##
    def drawTileContent(self):
        for i in range(map.ROWCOUNT):
            for j in range(map.COLUMNCOUNT):
                self.tiles[i][j].draw()

    def getSelectedTile(self, x, y):
        for row in self.tiles:
            for tile in row:
                if(tile.mouseInIt(x, y)): return tile
        return None

    #######################################################
    def draw(self):
        self.drawTileContent()
        self.drawGridLines()

    def selectUnitToMove(self, origX, origY): #some states and variables may need to be set in the controller during this process, I don't know
        if (not(tiles[origX][origY].tileEmpty()) and not(tiles[origX][origY].unit.isEnemy)):
            self.rangeTable[origX][origY]=1
            self.calculateRangeTable(origX, origY, self.tiles[origX][origY].unit.Movement)
            else: #The player clicked a tile with no unit or a unit they don't control
            pass

    def MoveUnit(self, origX, origY, newX, newY):
        if(self.rangeTable[newX][newY]==1):
            self.tiles[newX][newY].unit=self.tiles[origX][origY].unit
            self.tiles[origX][origY].unit=None
            fatigueAdded=newX-origX+newY-origY
            fatigueAdded=abs(fatigueAdded)
            self.tiles[newX][newY].unit.fatigue+=fatigueAdded


    def combat(self, atkrX, atkrY, dfdrX, dfdrY): #pass it the unit that's attacking and the unit that's attacked
        atkr=self.tiles[atkrX][atkrY].unit
        dfdr=self.tiles[dfdrX][dfdrY].unit
        #Attacker does his hit
        hitChanceAtkr=70+atkr.Skill-self.tiles[dfdrX][dfdrY].type[3]
        dfdrEffectiveDefense=dfdr.Defense-atkr.skill/2+self.tiles[dfdrX][dfdrY].type[2]
        if(dfdrEffectiveDefense<0): #no negative defense allowed
            dfdrEffectiveDefense=0
        if(dfdrEffectiveDefense%1 != 0):#no decimal point defense allowed
            dfdrEffectiveDefense+=0.5

        dmg1=atkr.Attack-dfdrEffectiveDefense
        if(dmg1<0): #no attack is allowed to do negative damage (would heal the target)
            dmg1=0

        rn=random.randint(0,99)
        if(rn<hitChanceAtkr):
            dfdr.HP-=dmg1
            atkr.fatigue+=1
        else:
            dfdr.fatigue+=1
            
        #defender does his hit if he lives
        if(dfdr.HP>0):
            hitChanceDfdr=70+dfdr.Skill-self.tiles[atkrX][atkrY].type[3]
            atkrEffectiveDefense=atkr.Defense-dfdr.skill/2+self.tiles[atkrX][atkrY].type[2]
            if(atkrEffectiveDefense<0):
                dfdrEffectiveDefense=0
            if(atkrEffectiveDefense%1 != 0):
                dfdrEffectiveDefense+=0.5

            dmg2=dfdr.Attack-atkrEffectiveDefense
            if(dmg2<0):
                dmg2=0

            rn=random.randint(0,99)
            if(rn<hitChanceDfdr):
                atkr.HP-=dmg2
                dfdr.fatigue+=1
            else:
                atkr.fatigue+=1

            #if attacker is still alive decide if anyone makes a second attack
            if(atkr.HP>0):
                if(atkr.Speed>dfdr.Speed):
                    rn=random.randint(0,99)
                    if(rn<hitChanceAtkr):
                        dfdr.HP-=dmg1
                        atkr.fatigue+=1
                    else:
                        dfdr.fatigue+=1
                elif(atkr.Speed<dfdr.Speed):
                    rn=random.randint(0,99)
                    if(rn<hitChanceDfdr):
                        atkr.HP-=dmg2
                        dfdr.fatigue+=1
                    else:
                        atkr.fatigue+=1
        if(atkr.HP<=0):
            tiles[atkrX][atkrY].unit=None #there will probably be a function here later for calculating exp gain
        elif(dfdr.HP<=0):
            tiles[dfdrX][dfdrY].unit=None #there will probably be a function here later for calculating exp gain

    
    
    def endTurn(self):
        if turn==1:
            turn=2
        elif turn==2:
            turn=1
            for i in range(map.ROWCOUNT):
                for j in range(map.COLUMNCOUNT):
                    if(self.tiles[i][j].unit!=None):
                        if(self.tiles[i][j].unit.fatigue>0):
                            self.tiles[i][j].unit.fatigue-=1
        return self.isClear() #if endTurn returns true then the level is over.

    def enemyAIUnitSelect(self):
        enemyList=[]
        for i in range(map.ROWCOUNT):
            for j in range(map.COLUMNCOUNT):
                if(self.tiles[i][j].unit!=None):
                    if(self.tiles[i][j].unit.isEnemy):
                        if(self.tiles[i][j].unit.fatigue<self.tiles[i][j].unit.maxFatigue):
                            #if(self.tiles[i][j].unit  #check that enemy type is not "wait" here
                            enemyData=[self.tiles[i][j].unit, i, j]
                            enemyList.append(enemyData)

        newEList=[]
        minFatigue=100 #Can an enemy attack? If so we're moving the one with the lowest fatigue to attack.
        for ENEMY in enemyList:
            self.constructEnemyRangeTable(ENEMY[1], ENEMY[2], ENEMY[0].Movement, 1)
            if self.enemyCanAttack:
                if(ENEMY[0].fatigue==minFatigue):
                    newEList.append(ENEMY)
                elif(ENEMY[0].fatigue<minFatigue):
                    newEList.Clear()
                    newEList.append(ENEMY)
                    minFatigue=ENEMY[0].fatigue
            self.clearRangeTables()


        if len(newEList)==0:
            newEList.Clear()
            minFatigue=100
            for ENEMY in enemyList:
                #if enemy AI type is attack
                    if(ENEMY[0].fatigue==minFatigue):
                        newEList.append(ENEMY)
                    elif(ENEMY[0].fatigue<minFatigue):
                        newEList.Clear()
                        newEList.append(ENEMY)
                        minFatigue=ENEMY[0].fatigue

        if len(newEList==0):
            self.endTurn()
        else:
            selectedEnemy=newEList[0]
            self.enemyMove(selectedEnemy[0], selectedEnemy[1], selectedEnemy[2])

    def enemyMove(self, se, x, y): #se for selected enemy
        self.constructEnemyRangeTable(x, y, se.Movement, 1)
        attackTargets=[]
        if self.enemyCanAttack:
            for i in range(map.ROWCOUNT):
                for j in range(map.COLUMNCOUNT):
                    if self.atkRangeTable[j][i]==1:
                        target=[j , i]
                        attackTargets.append(target)
            minHP=1000
            abcd=[]
            for t in attackTargets:
                if minHP==self.tiles[t[0]][t[1]].unit.HP:
                    toAppend=[t[0], t[1]]
                    abcd.append(toAppend)
                elif minHP>self.tiles[t[0]][t[1]].unit.HP:
                    abcd.Clear()
                    toAppend=[t[0], t[1]]
                    abcd.append(toAppend)
                    minHP=self.tiles[t[0]][t[1]].unit.HP
            t=attackTargets[0]
            X=t[0]
            Y=t[1]
            if(self.rangeTable[X-1][Y]==1):
                self.moveUnit(x, y, X-1, Y)
                self.combat(X-1, Y, X, Y)
            elif(self.rangeTable[X+1][Y]==1):
                self.moveUnit(x, y, X+1, Y)
                self.combat(X+1, Y, X, Y)
            elif(self.rangeTable[X][Y-1]==1):
                self.moveUnit(x, y, X, Y-1)
                self.combat(X, Y-1, X, Y)
            elif(self.rangeTable[X][Y+1]==1):
                self.moveUnit(x, y, X, Y+1)
                self.combat(X, Y+1, X, Y)
        else:
            found=False
            for i in range(map.ROWCOUNT):
                for j in range(map.COLUMNCOUNT):
                    if(not(self.tiles[i][j].tileEmpty())):
                        if self.tiles[i][j].unit.isEnemy:
                            found=True
                            break
                if found:
                    break
            mov=se.Movement
            if i<x:
                while(x>=0 and (mov-self.tiles[x-1][y].type[1])>=0):
                    moveUnit(x, y, x-1, y)
                    x-=1
                    mov-=self.tiles[x-1][y].type[1]
            elif i>x:
                while(x<=map.ROWCOUNT and (mov-self.tiles[x+1][y].type[1])>=0):
                    moveUnit(x, y, x+1, y)
                    x+=1
                    mov-=self.tiles[x+1][y].type[1]
            if j<y:
                while(y>=0 and (mov-self.tiles[x][y-1].type[1])>=0):
                    moveUnit(x, y, x, y-1)
                    y-=1
                    mov-=self.tiles[x][y-1].type[1]
            elif j>y:
                while(y<=map.COLUMNCOUNT and (mov-self.tiles[x][y-1].type[1])>=0):
                    moveUnit(x, y, x, y+1)
                    y+=1
                    mov-=self.tiles[x][y+1].type[1]
            
        self.endTurn()
                
            
            



'''
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
a.tiles[2][2].unit=Unit("Test.jpg", "Test Description", 0, 1, 2, 3, 4, 5, 6)
a.constructRangeTable(2, 2, 2)#A unit with 2 movement starting from the middle tile
for i in range(5):
    print(a.rangeTable[i])

a.tiles[2][3].unit=Unit("Test.jpg", "Test Description", 0, 1, 2, 3, 4, 5, 6)
a.clearRangeTables()
a.constructRangeTable(2, 2, 2) #the same move but now a friendly unit is to the right of our unit.
print("")
for i in range(5):
    print(a.rangeTable[i])
a.clearRangeTables()

a.tiles[2][2].unit.isEnemy=True
a.constructEnemyRangeTable(2, 2, 2, 1) #an enemy wants to move who has 2 movement and an attack range of 1.
print("")
for i in range(5):
    print(a.rangeTable[i])

print("Range Table")
for i in range(5):
    print(a.atkRangeTable[i])

a.clearRangeTables()
#a=map("level1.txt")
#a.enemies=1
#print(a.isClear())
#a.enemies-=1
#print(a.isClear())'''

