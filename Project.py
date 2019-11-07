import pygame

class Unit:
    def __init__(self, img_name, description, hp, attack, defense, skill, speed, xp, movement):
       super(type(img_name))                     
       self.HP = hp
       self.Attack = attack
       self.Defense = defense
       self.Skill = skill
       self.Speed = speed
       self.XP = xp
       self.Movement = movement
       self.Type = description

    def getX(self):
        return super.getX()

    def getY(self):
        return super.getY()

    def setX(self, x):
        return super.setX(x)

    def setY(self, y):      
        return super.setY(y)     

    #def update(Graphics g):                ???
        #super.update(g)

# -------------------------------------
# Main
# -------------------------------------
test = Unit("Test.jpg", "Test Description", 0, 1, 2, 3, 4, 5, 6)
print("HP = " + str(test.HP))
print("Attack = " + str(test.Attack))
print("Defense = " + str(test.Defense))
print("Skill = " + str(test.Skill))
print("Speed = " + str(test.Speed))
print("XP = " + str(test.XP))
print("Movement = " + str(test.Movement))
print("Type = " + str(test.Type))