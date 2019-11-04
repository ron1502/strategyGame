import json
from Game.gameElements.sprite import sprite

class model:
    def __init__(self):
        self.sprites = []
        self.run = True
        # Sprite for collision and event testing
        self.mainSprite = sprite(10, 10, 50, 50, r"\resources\sprites\link.png")
        self.anotherSprite =  sprite (100, 100, 20, 20)
        self.addSprite(self.mainSprite)
        self.addSprite(self.anotherSprite)

    def addSprite(self, sprite):
        self.sprites.append(sprite)

    def removeSprite(self, sprite):
        self.Sprites.remove(sprite)

    def loadGame(self):
        pass

    def saveGame(self):
        pass

    def update(self):
        if self.mainSprite.collide(self.anotherSprite):
            print("Collision is happening")
        # Check for collision if needed
        pass
