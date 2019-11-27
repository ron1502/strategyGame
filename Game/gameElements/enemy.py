from Game.gameElements.unit import Unit

class Enemy(Unit):

    def __init__(self, x, y, w, h, img_name, description, hp, attack, defense, xp, 
                fatigue, currentLvl, xp_to_next_lvl, isEnemy = True):
        super().__init__(x, y, w, h, img_name, description, hp, attack, defense, xp, 
                fatigue, currentLvl, xp_to_next_lvl)
        self.isEnemy = True

# Test Cases
# ---------------------------------------------------------------------------------
'''
xVal = 1
yVal = 2
wVal = 3
hVal = 4
sqrtPath = r"\resources\sprites\link.png" # Change this after we find a sprite for enemy
name = "Enemy"
lvl = 1
exp = 0
expNext = 10
hp = 10
hpMax = 10
attack = 1
defense = 1
fatigue = 1

test = Enemy(xVal, yVal, wVal, hVal, sqrtPath, name, lvl, exp, expNext, hp, hpMax, attack, defense, fatigue)

print("--------------------------------")
test.getInformation()
'''
