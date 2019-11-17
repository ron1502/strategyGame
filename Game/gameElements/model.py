import json
from Game.gameElements.sprite import sprite
from Game.gameElements.map import map
from Game.gameElements.unitMenu import unitMenu
from Game.gameElements.button import button


class model:
    def __init__(self):
        self.sprites = []
        self.run = True

        self.unitMenu = unitMenu(830, 0, 250, 720)
        # Sprite for collision and event testing
        self.map = map("")
        self.addSprite(self.map)
        self.addSprite(self.unitMenu)
        self.sprites += self.unitMenu.getButtons()
        
        self.selectedTile = None
        self.tileControlledUnit = None
        self.tileDefendingUnit = None
    def addSprite(self, sprite):
        self.sprites.append(sprite)

    def removeSprite(self, sprite):
        self.Sprites.remove(sprite)

    def checkClick(self, x, y):
        for sprt in self.sprites:
            if(isinstance(sprt, button)):
                if(sprt.checkClick(x, y)):
                    print(self.unitMenu.action)
                    
        self.selectedTile = self.map.getSelectedTile(x, y)
        if(self.selectedTile != None):
            if(self.selectedTile.unit != None):
                if(self.tileControlledUnit == None):
                    #Tile can only be controlled if ally or controll unit is empty
                    self.tileControlledUnit =  self.selectedTile
                    self.tileControlledUnit.selected = True
                elif(not self.selectedTile.unit.isEnemy):
                    self.tileControlledUnit.selected = False
                    self.tileControlledUnit =  self.selectedTile
                    self.tileControlledUnit.selected = True
                else:
                    if(self.unitMenu.action == "A"):
                        #Enemy can only be selected if action == Attack
                        self.tileDefendingUnit = self.selectedTile
                        #Hayce: self.map.attack(self.tileControlledUnit, self.tileDefendingUnit)
                        #Attack successfully performed (Turn ends)
                        self.tileControlledUnit.selected = False
                        self.unitMenu.action = None
                        self.tileControlledUnit = None
                    else:
                        print("Action can't be performed")
            elif(self.tileControlledUnit != None and self.unitMenu.action == "W"):
                #Hong: Check if unit can move to selected tile
                #Moving to tile
                self.selectedTile.unit = self.tileControlledUnit.unit
                self.tileControlledUnit.selected = False
                self.tileControlledUnit.unit = None
                

    def loadGame(self):
        pass

    def saveGame(self):
        pass

    def update(self):
        # Makes button clicking animation work
        for button in self.unitMenu.getButtons():
            button.update()
