import pygame

class Medium(Unit):
    def __init__(self):
        super("medium.jpg", "Medium", 100, 99, 99, 99, 99, 99, 99, 99)
        self.xpos = super.getX()
        self.ypos = super.getY()

    def update(self):
        self.xpos = super.getX()
        self.ypos = super.getY()
        self.pygame.display.update()

# Add getters for each variable