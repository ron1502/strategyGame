
from Game.gameElements.button import button
from Game.gameElements.sprite import sprite
import pygame

class menu:
    LIGHTGREY = pygame.Color(190, 193, 198)
    BLACK = pygame.Color(0,0,0)
    WHITE = pygame.Color(255,255,255)
    DARKGREY = pygame.Color(77, 77, 77)

    #title = pygame.image.load(path.join(img_dir, "The_Lonely_Shooter.png")).convert_alpha()
    #title = pygame.transform.scale(title, (WINDOWWIDTH, 81 * 2))
    

    def __init__(self):
        self.action = None
        self.go = button(465, 150, 150, "S", "Start Game", self.goFunct, menu.LIGHTGREY)
        self.quit = button(465, 250, 150, "S", "Quit", self.quitFunct, menu.LIGHTGREY)
        #self.background = loadImg(r"\resources\sprites\menu\background.png")
        #self.background_rect = background.get_rect()

    def goFunct(self):
        self.action = "G"

    def quitFunct(self):
        self.action = "Q"

    def getButtons(self):
        return (self.go, self.quit)