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
        self.height=0
        self.width=0
        self.enemies=0
        self.clearCondition=0
        self.tiles=[[]]
        self.turn=1 #it's 1 when player's turn 2 when enemy's turn.

    def isClear(self):
        func=clearSwitcher.get(self.clearCondition, "nothing")
        return func(self)
        
#a=map("level1.txt")
#a.enemies=1
#print(a.isClear())
#a.enemies-=1
#print(a.isClear())
