from Game.gameElements.sprite import sprite
from Game.gameElements.button import button
import pygame

class unitMenu(sprite):

    BUTTONCOLOR = pygame.Color(128, 103, 59)
    BGCOLOR = pygame.Color(165, 153, 126)

    
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h, )
        self.rect = pygame.Rect(x, y, w, h)
        self.action = None
        self.attackB = button(x, 50, w, "S", "Attack", self.attackFunct, unitMenu.BUTTONCOLOR)
        self.itemsB = button(x, 150, w, "S", "Items", self.itemsFunct, unitMenu.BUTTONCOLOR)
        self.walkB = button(x, 250, w, "S", "Walk", self.walkFunct, unitMenu.BUTTONCOLOR)
        self.endTurnB = button(x, 600, w, "S", "End Turn", self.endTurn, unitMenu.BUTTONCOLOR)

        self.attackB.setActive(False)

    def getButtons(self):
        return (self.attackB, self.itemsB, self.walkB, self.endTurnB)

    # Functions to modify the current actions
    def attackFunct(self):
        self.action = "A"

    def walkFunct(self):
        self.action = "W"

    def itemsFunct(self):
        self.action = "I"

    def endTurn(self):
        self.action = "E"
    ###########################################
    
    def draw(self):
        pygame.draw.rect(sprite.screen, unitMenu.BGCOLOR, self.rect)
