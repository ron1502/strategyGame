import json
from Game.gameElements.sprite import sprite
from  Game.gameElements.map import map

class model:
    def __init__(self):
        self.sprites = []
        self.run = True
        # Sprite for collision and event testing
        self.map = map("")
        self.addSprite(self.map)
        

    def addSprite(self, sprite):
        self.sprites.append(sprite)

    def removeSprite(self, sprite):
        self.Sprites.remove(sprite)

    def loadGame(self):
        pass

    def saveGame(self):
        pass

    def update(self):
        pass
