import pygame
from Game.gameElements.sprite import sprite

class stats(sprite):
    FONT = None
    FONTCOLOR = pygame.Color(255, 255, 255)
    BGCOLOR = pygame.Color(128, 103, 59)
    MARGIN = 20
    TXTSPACING = 20
    
    def __init__(self, x, y, w):
        super().__init__(x + stats.MARGIN//2, y, w - stats.MARGIN, 200)
        if(stats.FONT == None):
            stats.FONT =pygame.font.SysFont('Berlin Sans FB', 20)
        self.cleanFields()

    def cleanFields(self):
        self.title = stats.FONT.render("Stats( )", True, stats.FONTCOLOR)
        self.hp = stats.FONT.render("HP :", True, stats.FONTCOLOR)
        self.attack = stats.FONT.render("Attack :", True, stats.FONTCOLOR)
        self.defense = stats.FONT.render("Defense :", True, stats.FONTCOLOR)
        self.skill = stats.FONT.render("Skill :", True, stats.FONTCOLOR)
        self.xp = stats.FONT.render("XP:", True, stats.FONTCOLOR)

    def setUnit(self, unit):
        if(unit.isEnemy): self.txtTitle = "Stats(Enemy)"
        else: self.txtTitle = "Status(Ally)"
        self.title = stats.FONT.render(self.txtTitle, True, stats.FONTCOLOR)
        self.hp = stats.FONT.render("HP:          " + str(unit.HP), True, stats.FONTCOLOR)
        self.attack = stats.FONT.render("Attack:    " + str(unit.Attack), True, stats.FONTCOLOR)
        self.defense = stats.FONT.render("Defense:  " + str(unit.Defense), True, stats.FONTCOLOR)
        self.skill = stats.FONT.render("Skill:         " + str(unit.Skill), True, stats.FONTCOLOR)
        self.xp = stats.FONT.render("XP:           " + str(unit.XP), True, stats.FONTCOLOR)

    def draw(self):
        self.drawSquare(stats.BGCOLOR)
        self.screen.blit(self.title, (self.rect.x + 10, self.rect.y + stats.TXTSPACING))
        self.screen.blit(self.hp, (self.rect.x + 20, self.rect.y + stats.TXTSPACING*2))
        self.screen.blit(self.attack, (self.rect.x + 20, self.rect.y + stats.TXTSPACING*3))
        self.screen.blit(self.defense, (self.rect.x + 20, self.rect.y + stats.TXTSPACING*4))
        self.screen.blit(self.skill, (self.rect.x + 20, self.rect.y + stats.TXTSPACING*5))
        self.screen.blit(self.xp, (self.rect.x + 20, self.rect.y + stats.TXTSPACING*6))

    def update(self):
        pass
