from Game.gameElements.button import button
import pygame

class menu:
    LIGHTGREY = pygame.Color(190, 193, 198)
    BLACK = pygame.Color(0,0,0)
    WHITE = pygame.Color(255,255,255)
    DARKGREY = pygame.Color(77, 77, 77)

    def __init__(self):
        self.action = None
        self.go = button(465, 150, 150, "S", "Go", self.goFunct, menu.LIGHTGREY)
        self.quit = button(465, 250, 150, "S", "Quit", self.quitFunct, menu.LIGHTGREY)

    def goFunct(self):
        self.action = "G"

    def quitFunct(self):
        self.action = "Q"

    def getButtons(self):
        return (self.go, self.quit)
