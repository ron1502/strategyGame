import pygame

class Unit:
    def __init__(self, img_name, description, hp, attack, defense, skill, speed, xp, movement):
       super(img_name)
       self.HP = hp
       self.Attack = attack
       self.Defense = defense
       self.Skill = skill
       self.Speed = speed
       self.XP = xp
       self.Movement = movement
       self.Type = description

    def getX():
        return super.getX()

    def getY():
        return super.getY()

    def setX(x):
        newX = x
        super.setX(newX)

    def setY(y):      
        newY = y
        super.setY(newY)      

    def update(Graphics g):
        super.update(g)


# -------------------------------------
# Main
# -------------------------------------