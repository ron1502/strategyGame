from Game.gameElements.sprite import sprite
from Game.gameElements.button import button
from Game.gameElements.stats import stats
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
        self.stats = stats(x, 350, w)
        self.endTurnB = button(x, 600, w, "S", "End Turn", self.endTurn, unitMenu.BUTTONCOLOR)

        #Deactivation of button
        #   self.attackB.setActive(False)

    def setUnit(self, unit):
        self.stats.setUnit(unit)
        #Enable or desable certain buttons
        
    def getButtons(self):
        return (self.attackB, self.itemsB, self.walkB, self.endTurnB)

    def getStatsSprite(self):
        return self.stats

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
