import pygame

class Heavy(Unit):
    def __init__(self):
        super("heavy.jpg", "Medium", 1, 1, 1, 1, 1, 1, 1, 1)
        self.xpos = super.getX()
        self.ypos = super.getY()

    def update(self):
        self.xpos = super.getX()
        self.ypos = super.getY()
        self.pygame.display.update()

# Add getters for each variable