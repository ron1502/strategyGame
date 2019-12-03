import pygame
from Game.gameElements.sprite import sprite

class Unit(sprite):
    def __init__(self, x, y, w, h, img_name, description, hp, attack, defense, speed, xp, movement):
        ## w & h must be attributes of the image to load and not attributes of the tile
        super().__init__(x, y, w, h, img_name)
        self.HP = hp
        self.Attack = attack
        self.Defense = defense
        self.Speed = speed
        self.XP = xp
        self.Movement = movement


# -------------------------------------
# Main
# -------------------------------------
"""
test = Unit("Test.jpg", "Test Description", 0, 1, 2, 3, 4, 5, 6)
print("HP = " + str(test.HP))
print("Attack = " + str(test.Attack))
print("Defense = " + str(test.Defense))
print("Skill = " + str(test.Skill))
print("Speed = " + str(test.Speed))
print("XP = " + str(test.XP))
print("Movement = " + str(test.Movement))
print("Type = " + str(test.Type))
"""
